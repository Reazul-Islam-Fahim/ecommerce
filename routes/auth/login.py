from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.users.users import LoginSchema
from auth.login import login_user
from database.db import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(user: LoginSchema, db: Session = Depends(get_db)):
    return login_user(db, user)
