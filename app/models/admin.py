# app/models/admin.py
from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Admin(Base):
    __tablename__ = "admin"
    
    ID_Admin = Column(Integer, primary_key=True, index=True)
    Username_Admin = Column(String(50), unique=True, nullable=False)
    Password_Admin = Column(String(255), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)