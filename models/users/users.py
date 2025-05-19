from sqlalchemy import Column, Integer, String, Boolean, Enum as senum, ForeignKey, Computed, func
from sqlalchemy.orm import relationship
from database.db import Base
from enum import Enum

class roles(str, Enum):
    admin = "admin"
    user = "user"
    

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    role = Column(senum(roles), nullable=False, default=roles.user)
    is_active = Column(Boolean, nullable=False, default=True)
    is_verified = Column(Boolean, nullable=False, default=False)
    created_at = Column(String(50), nullable=False, server_default=func.now())
    updated_at = Column(String(50), nullable=False, server_default=func.now(), onupdate=func.now())