from fastapi import APIRouter, Depends, HTTPException, Request, Form  # type: ignore[import]
from fastapi.responses import HTMLResponse, RedirectResponse  # type: ignore[import]
from fastapi.templating import Jinja2Templates  # type: ignore[import]
from sqlalchemy.orm import Session
from core.database import get_db  # Sesuaikan dengan fungsi get_db kamu
from models.mahasiswa import Mahasiswa
from models.hasil_tes import HasilTes
from models.jenis_hasil_tes import JenisHasilTes
from collections import Counter

router = APIRouter(prefix="/mahasiswa", tags=["mahasiswa"])
templates = Jinja2Templates(directory="templates")

# Simulasi mendapatkan ID Mahasiswa dari session login (Sesuaikan dengan auth_utils kamu)
def get_current_mahasiswa_id(request: Request):
    # Contoh sederhana: mengambil dari cookies session
    mahasiswa_id = request.cookies.get("mahasiswa_id")
    if not mahasiswa_id:
        raise HTTPException(status_code=401, detail="Belum login")
    return int(mahasiswa_id)

### ================= DASHBOARD ================= ###
@router.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard(request: Request, db: Session = Depends(get_db), mhs_id: int = Depends(get_current_mahasiswa_id)):
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == mhs_id).first()
    
    # Ambil riwayat tes mahasiswa ini
    riwayat = db.query(HasilTes.ID_Jenis, JenisHasilTes.Hasil).\
        join(JenisHasilTes, HasilTes.ID_Jenis == JenisHasilTes.ID_Jenis).\
        filter(HasilTes.ID_Mahasiswa == mhs_id).all()
    
    # Hitung distribusi hasil untuk grafik lingkaran
    counts = Counter([r.Hasil for r in riwayat])
    labels = list(counts.keys())
    data_grafik = list(counts.values())
    
    return templates.TemplateResponse("DashMhs.html", {
        "request": request, 
        "mahasiswa": mahasiswa,
        "labels": labels,
        "data_grafik": data_grafik
    })

### ================= PROFIL (READ & UPDATE) ================= ###
@router.get("/profil", response_class=HTMLResponse)
async def view_profil(request: Request, db: Session = Depends(get_db), mhs_id: int = Depends(get_current_mahasiswa_id)):
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == mhs_id).first()
    return templates.TemplateResponse("Profil_Mahasiswa.html", {"request": request, "mahasiswa": mahasiswa})

@router.post("/profil/update")
async def update_profil(
    request: Request,
    nama: str = Form(...),
    alamat: str = Form(...),
    telepon: str = Form(...),
    email: str = Form(...),
    password_baru: str = Form(None),
    db: Session = Depends(get_db),
    mhs_id: int = Depends(get_current_mahasiswa_id)
):
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == mhs_id).first()
    if not mahasiswa:
        raise HTTPException(status_code=404, detail="Mahasiswa tidak ditemukan")
    
    # Update data biodata
    mahasiswa.Nama_Mahasiswa = nama
    mahasiswa.Alamat = alamat
    mahasiswa.Nomor_Telepon = telepon
    mahasiswa.Email = email
    
    # Jika password baru diisi, update password
    if password_baru and password_baru.strip() != "":
        mahasiswa.Password_Mahasiswa = password_baru # Catatan: Sebaiknya gunakan hashing di auth_utils
        
    db.commit()
    return RedirectResponse(url="/mahasiswa/profil", status_code=303)

### ================= RIWAYAT TES ================= ###
@router.get("/riwayat-tes", response_class=HTMLResponse)
async def view_riwayat(request: Request, db: Session = Depends(get_db), mhs_id: int = Depends(get_current_mahasiswa_id)):
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == mhs_id).first()
    
    # Ambil data riwayat lengkap beserta nama jenis kepribadiannya
    riwayat_tes = db.query(HasilTes.ID_Hasil, HasilTes.Waktu_Mulai_Tes, HasilTes.Waktu_Selesai_Tes, JenisHasilTes.Hasil).\
        join(JenisHasilTes, HasilTes.ID_Jenis == JenisHasilTes.ID_Jenis).\
        filter(HasilTes.ID_Mahasiswa == mhs_id).all()
        
    return templates.TemplateResponse("RiwayatTesMhs.html", {
        "request": request, 
        "mahasiswa": mahasiswa, 
        "riwayat_tes": riwayat_tes
    })