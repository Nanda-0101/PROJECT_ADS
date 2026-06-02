
# app/routes/kelola_admin.py

from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.responses import RedirectResponse, JSONResponse
from sqlalchemy.orm import Session
from starlette.status import HTTP_302_FOUND

from app.core.database import get_db
from app.models.admin import Admin

router = APIRouter(
    prefix="/kelola-admin",
    tags=["Kelola Admin"]
)

# =====================================================
# TAMBAH ADMIN
# =====================================================
@router.post("/tambah")
def tambah_admin(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    cek_username = (
        db.query(Admin)
        .filter(Admin.Username_Admin == username)
        .first()
    )

    if cek_username:
        raise HTTPException(
            status_code=400,
            detail="Username sudah digunakan"
        )

    cek_email = (
        db.query(Admin)
        .filter(Admin.Email == email)
        .first()
    )

    if cek_email:
        raise HTTPException(
            status_code=400,
            detail="Email sudah digunakan"
        )

    admin_baru = Admin(
        Username_Admin=username,
        Email=email,
        Password_Admin=password
    )

    db.add(admin_baru)
    db.commit()
    db.refresh(admin_baru)

    return RedirectResponse(
        url="/admin/kelola-admin",
        status_code=HTTP_302_FOUND
    )


# =====================================================
# HAPUS ADMIN
# =====================================================
@router.delete("/{id_admin}")
def hapus_admin(
    id_admin: int,
    db: Session = Depends(get_db)
):
    admin = (
        db.query(Admin)
        .filter(Admin.ID_Admin == id_admin)
        .first()
    )

    if not admin:
        raise HTTPException(
            status_code=404,
            detail="Admin tidak ditemukan"
        )

    db.delete(admin)
    db.commit()

    return JSONResponse(
        content={
            "message": "Admin berhasil dihapus"
        }
    )


# =====================================================
# EDIT ADMIN
# =====================================================
@router.post("/edit/{id_admin}")
def edit_admin(
    id_admin: int,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(""),
    db: Session = Depends(get_db)
):
    admin = (
        db.query(Admin)
        .filter(Admin.ID_Admin == id_admin)
        .first()
    )

    if not admin:
        raise HTTPException(
            status_code=404,
            detail="Admin tidak ditemukan"
        )

    admin.Username_Admin = username
    admin.Email = email

    if password.strip():
        admin.Password_Admin = password

    db.commit()

    return RedirectResponse(
        url="/admin/kelola-admin",
        status_code=HTTP_302_FOUND
    )


# =====================================================
# API DATA ADMIN
# =====================================================
@router.get("/api")
def get_admins(
    db: Session = Depends(get_db)
):
    admins = (
        db.query(Admin)
        .order_by(Admin.ID_Admin.asc())
        .all()
    )

    return [
        {
            "id": admin.ID_Admin,
            "username": admin.Username_Admin,
            "email": admin.Email
        }
        for admin in admins
    ]
