from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class DetailTes(Base):
    __tablename__ = "detail_tes"

    ID_Hasil = Column(Integer, ForeignKey("hasil_tes.ID_Hasil"), primary_key=True)
    ID_Soal = Column(Integer, ForeignKey("bank_soal.ID_Soal"), primary_key=True)
    Jawaban_Mahasiswa = Column(String(10))