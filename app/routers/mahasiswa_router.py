from fastapi import APIRouter, Depends, HTTPException, Request, Form  # type: ignore[import]
from fastapi.responses import HTMLResponse, RedirectResponse  # type: ignore[import]
from fastapi.templating import Jinja2Templates  # type: ignore[import]
from sqlalchemy.orm import Session

from app.core.database import get_db  # Sesuaikan dengan fungsi get_db kamu
from app.models.mahasiswa import Mahasiswa
from app.models.hasil_tes import HasilTes
from app.models.jenis_hasil_tes import JenisHasilTes
from collections import Counter

router = APIRouter(prefix="/mahasiswa", tags=["mahasiswa"])
templates = Jinja2Templates(directory="app/templates")

# Fungsi mendapatkan ID Mahasiswa dari session login cookie
def get_current_mahasiswa_id(request: Request):
    # Mengambil ID dari cookie 'mahasiswa_id' atau 'user_id' (sesuaikan dengan kode login Anda)
    mahasiswa_id = request.cookies.get("mahasiswa_id") or request.cookies.get("user_id")
    if not mahasiswa_id:
        raise HTTPException(status_code=401, detail="Belum login")
    return int(mahasiswa_id)

### ================= DASHBOARD ================= ###
@router.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard(request: Request, db: Session = Depends(get_db), mhs_id: int = Depends(get_current_mahasiswa_id)):
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == mhs_id).first()
    
    # 1. Ambil riwayat tes mahasiswa untuk grafik lingkaran
    riwayat = db.query(HasilTes.ID_Jenis, JenisHasilTes.Hasil).\
        join(JenisHasilTes, HasilTes.ID_Jenis == JenisHasilTes.ID_Jenis).\
        filter(HasilTes.ID_Mahasiswa == mhs_id).all()
    
    # Hitung distribusi hasil untuk grafik
    counts = Counter([r.Hasil for r in riwayat])
    
    # 2. Ambil data riwayat tes lengkap (Batas 3 atau 5 teratas untuk preview dashboard)
    #    Disertai eager load atau join dengan JenisHasilTes
    riwayat_tes = db.query(HasilTes).\
        join(JenisHasilTes, HasilTes.ID_Jenis == JenisHasilTes.ID_Jenis).\
        filter(HasilTes.ID_Mahasiswa == mhs_id).\
        order_by(HasilTes.Waktu_Selesai_Tes.desc()).limit(5).all()
    
    # Kirim parameter ke Jinja2 (Disamakan namanya dengan variabel di DashMhs.html)
    return templates.TemplateResponse("DashMhs.html", {
        "request": request, 
        "mahasiswa": mahasiswa,
        "grafik_labels": list(counts.keys()),  # Disamakan menjadi grafik_labels
        "grafik_data": list(counts.values()),  # Disamakan menjadi grafik_data
        "riwayat_tes": riwayat_tes             # Menyuplai riwayat tes singkat di dashboard
    })

### ================= PROFIL (READ & UPDATE) ================= ###
@router.get("/profil", response_class=HTMLResponse)
async def view_profil(
    request: Request, 
    msg_success: str = None, 
    msg_error: str = None, 
    db: Session = Depends(get_db), 
    mhs_id: int = Depends(get_current_mahasiswa_id)
):
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == mhs_id).first()
    return templates.TemplateResponse("Profil_Mahasiswa.html", {
        "request": request, 
        "mahasiswa": mahasiswa,
        "msg_success": msg_success,
        "msg_error": msg_error
    })

@router.post("/profil/update")
async def update_profil(
    request: Request,
    nama: str = Form(...),
    alamat: str = Form(None),
    telepon: str = Form(None),
    email: str = Form(None),
    deskripsi: str = Form(None), # Tambahan: menangkap Deskripsi dari database
    password_baru: str = Form(None),
    db: Session = Depends(get_db),
    mhs_id: int = Depends(get_current_mahasiswa_id)
):
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == mhs_id).first()
    if not mahasiswa:
        raise HTTPException(status_code=404, detail="Mahasiswa tidak ditemukan")
    
    try:
        # Update data berdasarkan nama kolom database asli Anda
        mahasiswa.Nama_Mahasiswa = nama
        mahasiswa.Alamat = alamat
        mahasiswa.Nomor_Telepon = telepon
        mahasiswa.Email = email
        mahasiswa.Deskripsi = deskripsi # Sinkron dengan nama kolom SQL
        
        # Jika password baru diisi, jalankan update password
        if password_baru and password_baru.strip() != "":
            mahasiswa.Password_Mahasiswa = password_baru
            
        db.commit()
        
        # Redirect kembali ke profil dengan parameter sukses
        response = RedirectResponse(url="/mahasiswa/profil?msg_success=Profil+berhasil+diperbarui", status_code=303)
        # Opsional: Update cookie nama agar nama di Top Navbar ikut langsung berubah
        response.set_cookie(key="user_nama", value=nama)
        return response

    except Exception as e:
        db.rollback()
        return RedirectResponse(url="/mahasiswa/profil?msg_error=Gagal+memperbarui+profil", status_code=303)

### ================= RIWAYAT TES ================= ###
@router.get("/riwayat", response_class=HTMLResponse)
async def riwayat_tes_mahasiswa(request: Request, db: Session = Depends(get_db)):
    # 1. Ambil Cookie Session
    user_role = request.cookies.get("user_role")
    user_id = request.cookies.get("mahasiswa_id") or request.cookies.get("user_id")
    
    if user_role != "mahasiswa" or not user_id:
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
    
    user_id = int(user_id)
    
    # 2. Ambil data mahasiswa dari DB untuk Top Bar
    mahasiswa = db.query(Mahasiswa).filter(Mahasiswa.ID_Mahasiswa == user_id).first()
    if not mahasiswa:
        return RedirectResponse(url="/", status_code=HTTP_302_FOUND)
        
    # 3. PERBAIKAN QUERY: Kita select kedua tabel sekaligus dalam bentuk tuple
    # Ini memastikan data HasilTes dan JenisHasilTes terikat dengan benar tanpa mengandalkan properti model
    daftar_riwayat = db.query(HasilTes, JenisHasilTes).\
        join(JenisHasilTes, HasilTes.ID_Jenis == JenisHasilTes.ID_Jenis).\
        filter(HasilTes.ID_Mahasiswa == user_id).\
        order_by(HasilTes.Waktu_Selesai_Tes.desc()).all()
        
    # 4. Kirim data ke HTML
    return templates.TemplateResponse(
        "RiwayatTesMhs.html", 
        {
            "request": request,
            "mahasiswa": mahasiswa,
            "daftar_riwayat": daftar_riwayat  # Berisi list dari tuple: [(HasilTes, JenisHasilTes), ...]
        }
    )