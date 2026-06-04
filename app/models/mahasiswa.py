# app/models/mahasiswa.py
from sqlalchemy import Column, Integer, String, Text, BigInteger
from sqlalchemy.sql import func
from app.core.database import Base

class Mahasiswa(Base):
    __tablename__ = "mahasiswa"
    
    ID_Mahasiswa = Column(Integer, primary_key=True, index=True)
    NIM = Column(BigInteger, unique=True, nullable=False)
    Nama_Mahasiswa = Column(String(100), nullable=False)
    Prodi = Column(String(100), nullable=True)
    Password_Mahasiswa = Column(String(255), nullable=False)
    Alamat = Column(Text, nullable=True)
    Nomor_Telepon = Column(String(20), nullable=True)
    Email = Column(String(100), unique=True, nullable=True)
    Deskripsi = Column(Text, nullable=True)
    created_by = Column(Integer, nullable=True)