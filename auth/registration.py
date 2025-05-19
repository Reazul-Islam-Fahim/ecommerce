from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.users.users import Users
from schemas.users.users import UserSchema
from fastapi import HTTPException
from auth.security import hash_password

def register_user(db: Session, user: UserSchema) -> Users:
    try:
        existing_user = db.query(Users).filter(Users.email == user.email).first()

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
            role=user.role
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )
