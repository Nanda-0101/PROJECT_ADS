from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base  # Sesuaikan dengan lokasi Base deklaratif Anda

class JenisHasilTes(Base):
    __tablename__ = "jenis_hasil_tes"

    # Sesuai SQL: `ID_Jenis` int(11) NOT NULL AUTO_INCREMENT
    ID_Jenis = Column(Integer, primary_key=True, autoincrement=True, index=True)
    
    # Sesuai SQL: `Hasil` varchar(50) NOT NULL (Menyimpan teks 'Introvert', 'Ekstrovert', 'Ambivert')
    Hasil = Column(String(50), nullable=False)

    # Relasi back-reference ke tabel hasil_tes (Opsional, untuk mempermudah ORM join)
    daftar_hasil_tes = relationship("HasilTes", back_populates="jenis_kepribadian")