from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.users.users import Users
from schemas.users.users import LoginSchema
from fastapi import HTTPException
from auth.security import verify_password, create_access_token

async def login_user(db: Session, user: LoginSchema) -> dict:
    try:
        db_user = await db.query(Users).filter(Users.email == user.email).first()

        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")

        if not verify_password(user.password, db_user.password):
            raise HTTPException(status_code=400, detail="Invalid credentials")

        token = create_access_token(
            data={
                "sub": db_user.email,
                "id": db_user.id,
                "role": db_user.role
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )
