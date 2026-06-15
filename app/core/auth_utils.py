from sqlalchemy.orm import Session
from sqlalchemy import text
from app.models.mahasiswa import Mahasiswa
from app.models.admin import Admin

def authenticate_mahasiswa(db: Session, nim: str, password: str):
    """Autentikasi mahasiswa berdasarkan NIM dan Password"""
    try:
        nim_int = int(nim) if nim.isdigit() else None

        mahasiswa = db.execute(
            text(
                "SELECT ID_Mahasiswa, NIM, Nama_Mahasiswa, Password_Mahasiswa "
                "FROM mahasiswa WHERE NIM = :nim LIMIT 1"
            ),
            {"nim": nim_int}
        ).mappings().first()

        if mahasiswa and mahasiswa["Password_Mahasiswa"] == password:
            return {
                "success": True,
                "role": "mahasiswa",
                "nama": mahasiswa["Nama_Mahasiswa"],
                "user_id": mahasiswa["ID_Mahasiswa"]
            }
        return None
    except Exception as e:
        print(f"Error authenticating mahasiswa: {e}")
        return None


def authenticate_admin(db: Session, username: str, password: str):
    """Autentikasi admin berdasarkan Username dan Password"""
    try:
        admin = db.query(Admin).filter(
            Admin.Username_Admin == username
        ).first()
        
        if admin and admin.Password_Admin == password:
            return {
                "success": True,
                "role": "admin",
                "nama": admin.Username_Admin,
                "user_id": admin.ID_Admin
            }
        return None
    except Exception as e:
        print(f"Error authenticating admin: {e}")
        return None