from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.users.users import UserSchema
from database.db import get_db
from auth.registration import register_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register(user: UserSchema, db: AsyncSession = Depends(get_db)):
    try:
        new_user = await register_user(db, user)
        
        await db.commit()
        
        print("User registered successfully:", new_user)
        
        return {
            "name": new_user.name,
            "email": new_user.email, 
            "dob": new_user.dob,
            "gender": new_user.gender,
            "phone": new_user.phone,
            "id": new_user.id, 
            "role": new_user.role,
            "isChecked": new_user.isChecked,
        }
        
    except HTTPException as e:
        await db.rollback()
        raise
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
    finally:
        await db.close() 