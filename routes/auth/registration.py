from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.users.users import UserSchema
from database.db import get_db
from auth.registration import register_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(user: UserSchema, db: Session = Depends(get_db)):
    
    new_user = register_user(db, user)
    
    return_data = {
        "name": new_user.name,
        "email": new_user.email, 
        "dob": new_user.dob,
        "gender": new_user.gender,
        "phone": new_user.phone,
        "id": new_user.id, 
        "role": new_user.role,
        "isChecked": new_user.isChecked,
        }

    return return_data
