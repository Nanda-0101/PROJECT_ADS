# app/routers/router.py
from fastapi import APIRouter, Request, Depends, HTTPException, Form, Body
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import func
from starlette.status import HTTP_302_FOUND

from app.core.database import get_db
from app.core.auth_utils import authenticate_mahasiswa, authenticate_admin
from app.models.mahasiswa import Mahasiswa
from app.models.admin import Admin
from app.models.tes import Tes
from app.models.bank_soal import BankSoal
from app.models.hasil_tes import HasilTes
from app.models.detail_tes import DetailTes
from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


# PAGE ROUTES

@router.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )


# LOGIN ENDPOINT

@router.post("/login")
async def login(
    request: Request,
    nim: str = Form(None),
    username: str = Form(None),
    password: str = Form(...),
    role: str = Form(...),
    db: Session = Depends(get_db)
):
    """Endpoint untuk login mahasiswa atau admin"""
    
    if role == "mahasiswa":
        if not nim:
            return templates.TemplateResponse(
                "login.html",
                {"request": request, "error": "NIM harus diisi"}
            )
        
        auth_result = authenticate_mahasiswa(db, nim, password)
        
        if auth_result and auth_result["success"]:
            # Set session or redirect
            response = RedirectResponse(
                url="/mahasiswa/dashboard",
                status_code=HTTP_302_FOUND
            )
            # Set cookie session 
            response.set_cookie(key="user_id", value=str(auth_result["user_id"]))
            response.set_cookie(key="user_role", value=auth_result["role"])
            response.set_cookie(key="user_nama", value=auth_result["nama"])
            return response
        else:
            return templates.TemplateResponse(
                "login.html",
                {"request": request, "error": "NIM atau Password salah"}
            )
    
    elif role == "admin":
        if not username:
            return templates.TemplateResponse(
                "login.html",
                {"request": request, "error": "Username harus diisi"}
            )
        
        auth_result = authenticate_admin(db, username, password)
        
        if auth_result and auth_result["success"]:
            response = RedirectResponse(
                url="/admin/dashboard",
                status_code=HTTP_302_FOUND
            )
            response.set_cookie(key="user_id", value=str(auth_result["user_id"]))
            response.set_cookie(key="user_role", value=auth_result["role"])
            response.set_cookie(key="user_nama", value=auth_result["nama"])
            return response
        else:
            return templates.TemplateResponse(
                "login.html",
                {"request": request, "error": "Username atau Password salah"}
            )
    
    else:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Role tidak valid"}
        )


# LOGOUT

@router.get("/logout")
async def logout():
    """Logout user"""
    response = RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    response.delete_cookie("user_id")
    response.delete_cookie("user_role")
    response.delete_cookie("user_nama")
    return response


# DASHBOARD ROUTES

@router.get("/mahasiswa/dashboard", response_class=HTMLResponse)
async def mahasiswa_dashboard(request: Request):
    # Check if user is logged in as mahasiswa
    user_role = request.cookies.get("user_role")
    if user_role != "mahasiswa":
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    
    return templates.TemplateResponse(
        "DashMhs.html",
        {
            "request": request,
            "nama": request.cookies.get("user_nama", "Mahasiswa")
        }
    )

@router.get("/mahasiswa/tes", response_class=HTMLResponse)
async def mahasiswa_tes(request: Request):
    # Check if user is logged in as mahasiswa
    user_role = request.cookies.get("user_role")
    if user_role != "mahasiswa":
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    
    return templates.TemplateResponse(
        "Tes_Mahasiswa.html",
        {
            "request": request,
            "nama": request.cookies.get("user_nama", "Mahasiswa")
        }
    )


@router.get("/mahasiswa/riwayat", response_class=HTMLResponse)
async def riwayat_tes(request: Request):
    user_role = request.cookies.get("user_role")
    if user_role != "mahasiswa":
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    
    return templates.TemplateResponse(
        "RiwayatTesMhs.html",
        {"request": request}
    )


@router.get("/mahasiswa/profil", response_class=HTMLResponse)
async def profil_mahasiswa(request: Request):
    user_role = request.cookies.get("user_role")
    if user_role != "mahasiswa":
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    
    return templates.TemplateResponse(
        "Profil_Mahasiswa.html",
        {"request": request}
    )


@router.get("/admin/dashboard", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    user_role = request.cookies.get("user_role")
    if user_role != "admin":
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    
    return templates.TemplateResponse(
        "admin_dashboard.html",
        {"request": request}
    )

@router.get("/admin/riwayat-tes", response_class=HTMLResponse)
async def admin_riwayat_tes(request: Request):
    user_role = request.cookies.get("user_role")
    if user_role != "admin":
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    return templates.TemplateResponse("admin_RiwayatTesMahasiswa.html", {"request": request})

@router.get("/admin/profil", response_class=HTMLResponse)
async def admin_profil(request: Request):
    user_role = request.cookies.get("user_role")
    if user_role != "admin":
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    return templates.TemplateResponse("Profil_Admin.html", {"request": request})

# ---- Admin API: Mahasiswa CRUD, Riwayat, Dashboard, Admin profile ----

@router.get("/api/mahasiswa")
def list_mahasiswa(db: Session = Depends(get_db)):
    rows = db.query(Mahasiswa).all()
    return [
        {
            "id": m.ID_Mahasiswa,
            "nim": int(m.NIM),
            "nama": m.Nama_Mahasiswa,
            "email": m.Email,
            "alamat": m.Alamat,
            "nomor_telepon": m.Nomor_Telepon,
            "deskripsi": m.Deskripsi,
            "created_by": m.created_by,
        }
        for m in rows
    ]


@router.post("/api/mahasiswa", status_code=201)
def create_mahasiswa(payload: dict = Body(...), db: Session = Depends(get_db)):
    mahasiswa = Mahasiswa(
        NIM=int(payload.get("NIM")),
        Nama_Mahasiswa=payload.get("Nama_Mahasiswa"),
        Password_Mahasiswa=payload.get("Password_Mahasiswa"),
        Alamat=payload.get("Alamat"),
        Nomor_Telepon=payload.get("Nomor_Telepon"),
        Email=payload.get("Email"),
        Deskripsi=payload.get("Deskripsi"),
        created_by=payload.get("created_by"),
    )
    db.add(mahasiswa)
    db.commit()
    db.refresh(mahasiswa)
    return {"success": True, "id": mahasiswa.ID_Mahasiswa}


@router.put("/api/mahasiswa/{id_mahasiswa}")
def update_mahasiswa(
    id_mahasiswa: int,
    payload: dict = Body(...),
    db: Session = Depends(get_db),
):
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == id_mahasiswa).first()
    if not mahasiswa:
        raise HTTPException(status_code=404, detail="Mahasiswa not found")

    if payload.get("NIM") is not None:
        mahasiswa.NIM = int(payload["NIM"])
    if payload.get("Nama_Mahasiswa") is not None:
        mahasiswa.Nama_Mahasiswa = payload["Nama_Mahasiswa"]
    if payload.get("Password_Mahasiswa") is not None:
        mahasiswa.Password_Mahasiswa = payload["Password_Mahasiswa"]
    if payload.get("Alamat") is not None:
        mahasiswa.Alamat = payload["Alamat"]
    if payload.get("Nomor_Telepon") is not None:
        mahasiswa.Nomor_Telepon = payload["Nomor_Telepon"]
    if payload.get("Email") is not None:
        mahasiswa.Email = payload["Email"]
    if payload.get("Deskripsi") is not None:
        mahasiswa.Deskripsi = payload["Deskripsi"]
    if payload.get("created_by") is not None:
        mahasiswa.created_by = payload["created_by"]

    db.commit()
    return {"success": True}


@router.delete("/api/mahasiswa/{id_mahasiswa}")
def delete_mahasiswa(id_mahasiswa: int, db: Session = Depends(get_db)):
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == id_mahasiswa).first()
    if not mahasiswa:
        raise HTTPException(status_code=404, detail="Mahasiswa not found")

    db.delete(mahasiswa)
    db.commit()
    return {"success": True}


@router.get("/api/riwayat")
def list_riwayat(db: Session = Depends(get_db)):
    rows = (
        db.query(HasilTes, Mahasiswa)
        .join(Mahasiswa, Mahasiswa.ID_Mahasiswa == HasilTes.ID_Mahasiswa)
        .order_by(HasilTes.ID_Hasil.desc())
        .all()
    )

    mapping = {1: "Introvert", 2: "Ekstrovert", 3: "Ambivert"}
    result = []
    for hasil, mahasiswa in rows:
        result.append(
            {
                "id_hasil": hasil.ID_Hasil,
                "nim": int(mahasiswa.NIM),
                "nama": mahasiswa.Nama_Mahasiswa,
                "tanggal": hasil.Waktu_Selesai_Tes.isoformat() if hasil.Waktu_Selesai_Tes else None,
                "id_jenis": hasil.ID_Jenis,
                "status": mapping.get(hasil.ID_Jenis, "Unknown"),
            }
        )
    return result


@router.get("/api/riwayat/{id_hasil}")
def riwayat_detail(id_hasil: int, db: Session = Depends(get_db)):
    rows = (
        db.query(DetailTes, BankSoal)
        .join(BankSoal, BankSoal.ID_Soal == DetailTes.ID_Soal)
        .filter(DetailTes.ID_Hasil == id_hasil)
        .order_by(DetailTes.ID_Soal)
        .all()
    )

    return [
        {
            "id_soal": detail.ID_Soal,
            "pertanyaan": soal.Pertanyaan,
            "jawaban": detail.Jawaban_Mahasiswa,
        }
        for detail, soal in rows
    ]


@router.get("/api/admin/summary")
def admin_summary(db: Session = Depends(get_db)):
    total_mahasiswa = db.query(func.count(Mahasiswa.ID_Mahasiswa)).scalar() or 0
    total_tes = db.query(func.count(HasilTes.ID_Hasil)).scalar() or 0

    counts = (
        db.query(HasilTes.ID_Jenis, func.count(HasilTes.ID_Jenis))
        .group_by(HasilTes.ID_Jenis)
        .all()
    )

    mapping = {1: "Introvert", 2: "Ekstrovert", 3: "Ambivert"}
    by_type = {mapping.get(id_jenis, str(id_jenis)): jumlah for id_jenis, jumlah in counts if id_jenis is not None}
    dominant = max(by_type, key=by_type.get) if by_type else None

    return {
        "total_mahasiswa": total_mahasiswa,
        "total_tes": total_tes,
        "by_type": by_type,
        "dominant": dominant,
    }


@router.get("/api/admin/profile")
def get_admin_profile(db: Session = Depends(get_db)):
    admin = db.query(Admin).order_by(Admin.ID_Admin).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    return {
        "id": admin.ID_Admin,
        "username": admin.Username_Admin,
        "email": admin.Email,
    }


@router.put("/api/admin/profile")
def update_admin_profile(payload: dict = Body(...), db: Session = Depends(get_db)):
    admin = db.query(Admin).order_by(Admin.ID_Admin).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    if payload.get("username") is not None:
        admin.Username_Admin = payload["username"]
    if payload.get("email") is not None:
        admin.Email = payload["email"]
    if payload.get("password"):
        admin.Password_Admin = payload["password"]

    db.commit()
    return {"success": True}

@router.get("/api/navigasi-mahasiswa")
async def get_navigasi_mahasiswa():
    from fastapi.responses import FileResponse
    return FileResponse("app/templates/Mahasiswa_Navigasi.html")

@router.get("/api/navigasi")
async def get_navigasi():
    from fastapi.responses import FileResponse
    return FileResponse("app/templates/admin_Navigasi.html")

# TEST DATABASE

@router.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    from app.models.mahasiswa import Mahasiswa
    from app.models.admin import Admin
    
    mahasiswa_count = db.query(Mahasiswa).count()
    admin_count = db.query(Admin).count()
    
    return {
        "status": "database connected",
        "mahasiswa_count": mahasiswa_count,
        "admin_count": admin_count
    }