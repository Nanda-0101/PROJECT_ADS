from sqlalchemy import Column, Integer, Text, ForeignKey
from app.core.database import Base

class BankSoal(Base):
    __tablename__ = "bank_soal"

    ID_Soal = Column(Integer, primary_key=True, index=True)
    ID_Tes = Column(Integer, ForeignKey("tes.ID_Tes"))
    Pertanyaan = Column(Text)