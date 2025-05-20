from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from models.users.users import Users
from schemas.users.users import UserSchema
from fastapi import HTTPException
from auth.security import hash_password

async def register_user(db: AsyncSession, user: UserSchema) -> Users:
    try:
        result = await db.execute(
            select(Users).where(Users.email == user.email)
        )
        existing_user = result.scalar_one_or_none()
        
        if existing_user:
            raise HTTPException(
                status_code=409,
                detail="Email already registered"
            )

        new_user = Users(
            name=user.name,
            email=user.email,
            password=hash_password(user.password),
            phone=user.phone,
            dob=user.dob,
            gender=user.gender,
            role=user.role,
            isChecked=user.isChecked
        )

        db.add(new_user)
        await db.flush() 
        
        return new_user

    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )