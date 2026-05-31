"""Router module: page routes + APIs for mahasiswa/admin/tes."""
from fastapi import APIRouter, Request, Depends, HTTPException, Form, Body
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse, JSONResponse
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
from app.models.jenis_hasil_tes import JenisHasilTes

from app.schemas.auth import LoginRequest, LoginResponse
from app.services.huggingface_service import predict_kepribadian

from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


# PAGE ROUTES
@router.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


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
    if role == "mahasiswa":
        if not nim:
            return templates.TemplateResponse("login.html", {"request": request, "error": "NIM harus diisi"})
        auth_result = authenticate_mahasiswa(db, nim, password)
        if auth_result and auth_result["success"]:
            response = RedirectResponse(url="/mahasiswa/dashboard", status_code=HTTP_302_FOUND)
            response.set_cookie(key="user_id", value=str(auth_result["user_id"]))
            response.set_cookie(key="user_role", value=auth_result["role"]) 
            response.set_cookie(key="user_nama", value=auth_result["nama"])
            return response
        else:
            return templates.TemplateResponse("login.html", {"request": request, "error": "NIM atau Password salah"})
    elif role == "admin":
        if not username:
            return templates.TemplateResponse("login.html", {"request": request, "error": "Username harus diisi"})
        auth_result = authenticate_admin(db, username, password)
        if auth_result and auth_result["success"]:
            response = RedirectResponse(url="/admin/dashboard", status_code=HTTP_302_FOUND)
            response.set_cookie(key="user_id", value=str(auth_result["user_id"]))
            response.set_cookie(key="user_role", value=auth_result["role"]) 
            response.set_cookie(key="user_nama", value=auth_result["nama"])
            return response
        else:
            return templates.TemplateResponse("login.html", {"request": request, "error": "Username atau Password salah"})
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Role tidak valid"})


# LOGOUT
@router.get("/logout")
async def logout():
    response = RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    response.delete_cookie("user_id")
    response.delete_cookie("user_role")
    response.delete_cookie("user_nama")
    return response


# DASHBOARD ROUTES
@router.get("/mahasiswa/dashboard", response_class=HTMLResponse)
async def mahasiswa_dashboard(request: Request, db: Session = Depends(get_db)):
    user_role = request.cookies.get("user_role")
    user_id = request.cookies.get("user_id")
    if user_role != "mahasiswa" or not user_id:
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    user_id = int(user_id)
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == user_id).first()
    if not mahasiswa:
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    riwayat_tes = db.query(HasilTes).filter(HasilTes.ID_Mahasiswa == user_id).order_by(HasilTes.Waktu_Selesai_Tes.desc()).all()
    statistik = db.query(JenisHasilTes.Hasil, func.count(HasilTes.ID_Hasil)).join(HasilTes, JenisHasilTes.ID_Jenis == HasilTes.ID_Jenis).filter(HasilTes.ID_Mahasiswa == user_id).group_by(JenisHasilTes.Hasil).all()
    grafik_labels = [row[0] for row in statistik]
    grafik_data = [row[1] for row in statistik]
    return templates.TemplateResponse("DashMhs.html", {"request": request, "mahasiswa": mahasiswa, "riwayat_tes": riwayat_tes, "grafik_labels": grafik_labels, "grafik_data": grafik_data})


@router.get("/mahasiswa/tes", response_class=HTMLResponse)
async def mahasiswa_tes(request: Request):
    user_role = request.cookies.get("user_role")
    if user_role != "mahasiswa":
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    return templates.TemplateResponse("Tes_Mahasiswa.html", {"request": request, "nama": request.cookies.get("user_nama", "Mahasiswa")})


@router.get("/mahasiswa/profil", response_class=HTMLResponse)
async def profil_mahasiswa(request: Request, msg_success: str = None, msg_error: str = None, db: Session = Depends(get_db)):
    user_role = request.cookies.get("user_role")
    user_id = request.cookies.get("user_id")
    if user_role != "mahasiswa" or not user_id:
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == int(user_id)).first()
    return templates.TemplateResponse("Profil_Mahasiswa.html", {"request": request, "mahasiswa": mahasiswa, "msg_success": msg_success, "msg_error": msg_error})


@router.post("/mahasiswa/profil/update")
async def update_profil_mahasiswa(request: Request, nama_mahasiswa: str = Form(...), email: str = Form(None), biodata: str = Form(None), password_baru: str = Form(None), db: Session = Depends(get_db)):
    user_role = request.cookies.get("user_role")
    user_id = request.cookies.get("user_id")
    if user_role != "mahasiswa" or not user_id:
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == int(user_id)).first()
    if not mahasiswa:
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    try:
        mahasiswa.Nama_Mahasiswa = nama_mahasiswa
        mahasiswa.Email = email
        mahasiswa.Biodata = biodata
        if password_baru and password_baru.strip() != "":
            mahasiswa.Password_Mahasiswa = password_baru
        db.commit()
        response = RedirectResponse(url="/mahasiswa/profil", status_code=HTTP_302_FOUND)
        response.set_cookie(key="user_nama", value=nama_mahasiswa)
        return response
    except Exception:
        db.rollback()
        return RedirectResponse(url="/mahasiswa/profil", status_code=HTTP_302_FOUND)


@router.get("/admin/dashboard", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    user_role = request.cookies.get("user_role")
    if user_role != "admin":
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    return templates.TemplateResponse("admin_dashboard.html", {"request": request})


@router.get("/admin/kelola-mahasiswa", response_class=HTMLResponse)
async def admin_kelola_mahasiswa(request: Request):
    user_role = request.cookies.get("user_role")
    if user_role != "admin":
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    return templates.TemplateResponse("admin_KelolaMahasiswa.html", {"request": request})


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
            "nim": int(m.NIM) if m.NIM is not None else None,
            "nama": m.Nama_Mahasiswa,
            "email": m.Email,
            "alamat": m.Alamat,
            "nomor_telepon": m.Nomor_Telepon,
            "deskripsi": m.Deskripsi,
            "created_by": getattr(m, 'created_by', None),
        }
        for m in rows
    ]


@router.post("/api/mahasiswa", status_code=201)
def create_mahasiswa(payload: dict = Body(...), db: Session = Depends(get_db)):
    mahasiswa = Mahasiswa(
        NIM=int(payload.get("NIM")) if payload.get("NIM") is not None else None,
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
def update_mahasiswa(id_mahasiswa: int, payload: dict = Body(...), db: Session = Depends(get_db)):
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
    rows = db.query(HasilTes, Mahasiswa).join(Mahasiswa, Mahasiswa.ID_Mahasiswa == HasilTes.ID_Mahasiswa).order_by(HasilTes.ID_Hasil.desc()).all()
    mapping = {1: "Introvert", 2: "Ekstrovert", 3: "Ambivert"}
    result = []
    for hasil, mahasiswa in rows:
        result.append({
            "id_hasil": hasil.ID_Hasil,
            "nim": int(mahasiswa.NIM) if mahasiswa.NIM is not None else None,
            "nama": mahasiswa.Nama_Mahasiswa,
            "tanggal": hasil.Waktu_Selesai_Tes.isoformat() if hasil.Waktu_Selesai_Tes else None,
            "id_jenis": hasil.ID_Jenis,
            "status": mapping.get(hasil.ID_Jenis, "Unknown"),
        })
    return result


@router.get("/api/riwayat/{id_hasil}")
def riwayat_detail(id_hasil: int, db: Session = Depends(get_db)):
    rows = db.query(DetailTes, BankSoal).join(BankSoal, BankSoal.ID_Soal == DetailTes.ID_Soal).filter(DetailTes.ID_Hasil == id_hasil).order_by(DetailTes.ID_Soal).all()
    return [{"id_soal": detail.ID_Soal, "pertanyaan": soal.Pertanyaan, "jawaban": detail.Jawaban_Mahasiswa} for detail, soal in rows]


@router.get("/api/admin/summary")
def admin_summary(db: Session = Depends(get_db)):
    total_mahasiswa = db.query(func.count(Mahasiswa.ID_Mahasiswa)).scalar() or 0
    total_tes = db.query(func.count(HasilTes.ID_Hasil)).scalar() or 0
    counts = db.query(HasilTes.ID_Jenis, func.count(HasilTes.ID_Jenis)).group_by(HasilTes.ID_Jenis).all()
    mapping = {1: "Introvert", 2: "Ekstrovert", 3: "Ambivert"}
    by_type = {mapping.get(id_jenis, str(id_jenis)): jumlah for id_jenis, jumlah in counts if id_jenis is not None}
    dominant = max(by_type, key=by_type.get) if by_type else None
    return {"total_mahasiswa": total_mahasiswa, "total_tes": total_tes, "by_type": by_type, "dominant": dominant}


@router.get("/api/admin/profile")
def get_admin_profile(db: Session = Depends(get_db)):
    admin = db.query(Admin).order_by(Admin.ID_Admin).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    return {"id": admin.ID_Admin, "username": admin.Username_Admin, "email": admin.Email}


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
    return FileResponse("app/templates/Mahasiswa_Navigasi.html")


@router.get("/api/navigasi")
async def get_navigasi():
    return FileResponse("app/templates/admin_Navigasi.html")


# TEST DATABASE
@router.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    from app.models.mahasiswa import Mahasiswa
    from app.models.admin import Admin
    mahasiswa_count = db.query(Mahasiswa).count()
    admin_count = db.query(Admin).count()
    return {"status": "database connected", "mahasiswa_count": mahasiswa_count, "admin_count": admin_count}


@router.get("/api/tes")
def get_tes(db: Session = Depends(get_db)):
    data = db.query(Tes).all()
    return [{"id": tes.ID_Tes, "nama": tes.Nama_Tes} for tes in data]


@router.get("/api/tes/{id_tes}/soal")
def get_soal(id_tes: int, db: Session = Depends(get_db)):
    soal = db.query(BankSoal).filter(BankSoal.ID_Tes == id_tes).all()
    return [{"id": s.ID_Soal, "text": s.Pertanyaan} for s in soal]


@router.post("/api/tes/submit")
async def submit_tes(request: Request, db: Session = Depends(get_db)):
    body = await request.json()
    id_tes = body["id_tes"]
    answers = body["answers"]
    user_id = request.cookies.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="User belum login")
    user_id = int(user_id)
    hasil = HasilTes(ID_Mahasiswa=user_id, ID_Tes=id_tes, Waktu_Mulai_Tes=datetime.now(), Waktu_Selesai_Tes=datetime.now())
    db.add(hasil)
    db.commit()
    db.refresh(hasil)
    mapping_jawaban = {"STS": 1, "TS": 2, "N": 3, "S": 4, "SS": 5}
    gender_raw = next(item["jawaban"] for item in answers if item["id_soal"] == 1)
    age_raw = next(item["jawaban"] for item in answers if item["id_soal"] == 2)
    gender = int(gender_raw)
    age = int(age_raw)
    jawaban_ml = []
    for item in answers:
        if 3 <= item["id_soal"] <= 93:
            nilai = mapping_jawaban.get(item["jawaban"], 3)
            jawaban_ml.append(nilai)
        if item["id_soal"] == 1 or item["id_soal"] == 2:
            db.add(DetailTes(ID_Hasil=hasil.ID_Hasil, ID_Soal=item["id_soal"], Jawaban_Mahasiswa=int(item["jawaban"])))
        else:
            nilai_int = mapping_jawaban.get(item["jawaban"], 3)
            db.add(DetailTes(ID_Hasil=hasil.ID_Hasil, ID_Soal=item["id_soal"], Jawaban_Mahasiswa=nilai_int))
    if len(jawaban_ml) != 91:
        raise HTTPException(status_code=400, detail=f"Jumlah jawaban ML harus 91, sekarang {len(jawaban_ml)}")
    hasil_prediksi, probabilitas = predict_kepribadian(gender=gender, age=age, jawaban=jawaban_ml)
    mapping = {"Introvert": 1, "Ekstrovert": 2, "Ambivert": 3}
    hasil.ID_Jenis = mapping.get(hasil_prediksi, 3)
    db.commit()
    return {"success": True, "hasil": hasil_prediksi, "probabilities": probabilitas}


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