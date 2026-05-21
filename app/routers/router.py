# app/routers/router.py
from fastapi import APIRouter, Request, Depends, HTTPException, Form
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.status import HTTP_302_FOUND

from app.core.database import get_db
from app.core.auth_utils import authenticate_mahasiswa, authenticate_admin
from app.models.mahasiswa import Mahasiswa
from app.schemas.auth import LoginRequest, LoginResponse

from app.models.tes import Tes
from app.models.bank_soal import BankSoal
from app.models.hasil_tes import HasilTes
from app.models.detail_tes import DetailTes

from app.services.huggingface_service import predict_kepribadian

from datetime import datetime
from fastapi.responses import JSONResponse

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

@router.get("/admin/kelola-mahasiswa", response_class=HTMLResponse)
async def admin_kelola_mahasiswa(request: Request):
    user_role = request.cookies.get("user_role")
    if user_role != "admin":
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    
    return templates.TemplateResponse(
        "admin_KelolaMahasiswa.html", 
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

@router.get("/api/tes")
def get_tes(db: Session = Depends(get_db)):
    data = db.query(Tes).all()

    return [
        {
            "id": tes.ID_Tes,
            "nama": tes.Nama_Tes
        }
        for tes in data
    ]

@router.get("/api/tes/{id_tes}/soal")
def get_soal(id_tes: int, db: Session = Depends(get_db)):

    soal = db.query(BankSoal)\
        .filter(BankSoal.ID_Tes == id_tes)\
        .all()

    return [
        {
            "id": s.ID_Soal,
            "text": s.Pertanyaan
        }
        for s in soal
    ]

@router.post("/api/tes/submit")
async def submit_tes(
    request: Request,
    db: Session = Depends(get_db)
):
    body = await request.json()

    id_tes = body["id_tes"]
    answers = body["answers"]

    user_id = request.cookies.get("user_id")

    if not user_id:
        raise HTTPException(status_code=401, detail="User belum login")

    user_id = int(user_id)

    # SIMPAN HASIL TES
    hasil = HasilTes(
        ID_Mahasiswa=user_id,
        ID_Tes=id_tes,
        Waktu_Mulai_Tes=datetime.now(),
        Waktu_Selesai_Tes=datetime.now()
    )

    db.add(hasil)
    db.commit()
    db.refresh(hasil)

    mapping_jawaban = {
        "STS": 1,
        "TS": 2,
        "N": 3,
        "S": 4,
        "SS": 5
    }

    # ambil gender & age dengan konversi ke int
    gender_raw = next(item["jawaban"] for item in answers if item["id_soal"] == 1)
    age_raw = next(item["jawaban"] for item in answers if item["id_soal"] == 2)
    
    gender = int(gender_raw) 
    age = int(age_raw) 
    
    # ambil hanya Q1 - Q91
    jawaban_ml = []
    for item in answers:
        if 3 <= item["id_soal"] <= 93:   
            nilai = mapping_jawaban.get(item["jawaban"], 3)
            jawaban_ml.append(nilai)
   
        # simpan semua ke DB sebagai 
        if item["id_soal"] == 1 or item["id_soal"] == 2:
            # Gender dan age simpan sebagai 
            db.add(
                DetailTes(
                    ID_Hasil=hasil.ID_Hasil,
                    ID_Soal=item["id_soal"],
                    Jawaban_Mahasiswa=int(item["jawaban"])  
                )
            )
        else:
            # Untuk Q3-Q93, simpan  (1-5)
            nilai_int = mapping_jawaban.get(item["jawaban"], 3)
            db.add(
                DetailTes(
                    ID_Hasil=hasil.ID_Hasil,
                    ID_Soal=item["id_soal"],
                    Jawaban_Mahasiswa=nilai_int  
                )
            )

    # VALIDASI JUMLAH FITUR
    if len(jawaban_ml) != 91:
        raise HTTPException(
            status_code=400,
            detail=f"Jumlah jawaban ML harus 91, sekarang {len(jawaban_ml)}"
        )

    # PREDIKSI ML
    hasil_prediksi, probabilitas = predict_kepribadian(
        gender=gender,
        age=age,
        jawaban=jawaban_ml
    )

    mapping = {
        "Introvert": 1,
        "Ekstrovert": 2,
        "Ambivert": 3
    }

    hasil.ID_Jenis = mapping.get(hasil_prediksi, 3)

    db.commit()

    return {
        "success": True,
        "hasil": hasil_prediksi,
        "probabilities": probabilitas
    }