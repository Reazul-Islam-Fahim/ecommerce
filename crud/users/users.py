from sqlalchemy.orm import Session, Query
from models.users.users import Users
from schemas.users.users import UserSchema
from fastapi import HTTPException
from sqlalchemy import desc

def get_user(db: Session, id: int):
    return db.query(Users).filter(Users.id == id).first()

def get_users(db: Session, skip: int = 0, limit: int = Query(...)):  
    return db.query(Users).offset(skip).limit(limit).all()

def update_user(db: Session, id: int, user: UserSchema):
    db_user = db.query(Users).filter(Users.id == id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_user.name = user.name
    db_user.email = user.email
    db_user.password = user.password
    db_user.phone = user.phone
    db_user.dob = user.dob
    db_user.gender = user.gender
    
    db.commit()
    db.refresh(db_user)
    return db_user