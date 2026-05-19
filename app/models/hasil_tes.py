from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP
from app.core.database import Base

class HasilTes(Base):
    __tablename__ = "hasil_tes"

    ID_Hasil = Column(Integer, primary_key=True, index=True)
    ID_Mahasiswa = Column(Integer)
    ID_Tes = Column(Integer)
    ID_Jenis = Column(Integer, nullable=True)
    Waktu_Mulai_Tes = Column(TIMESTAMP)
    Waktu_Selesai_Tes = Column(TIMESTAMP)