from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Tes(Base):
    __tablename__ = "tes"

    ID_Tes = Column(Integer, primary_key=True, index=True)
    Nama_Tes = Column(String(100))
    Jumlah_Soal = Column(Integer)