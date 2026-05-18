from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


# LOGIN
@router.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )


# DASHBOARD MAHASISWA
@router.get("/mahasiswa/dashboard", response_class=HTMLResponse)
async def mahasiswa_dashboard(request: Request):
    return templates.TemplateResponse(
        "DashMhs.html",
        {"request": request}
    )


# RIWAYAT TES
@router.get("/mahasiswa/riwayat", response_class=HTMLResponse)
async def riwayat_tes(request: Request):
    return templates.TemplateResponse(
        "RiwayatTesMhs.html",
        {"request": request}
    )


# PROFIL MAHASISWA
@router.get("/mahasiswa/profil", response_class=HTMLResponse)
async def profil_mahasiswa(request: Request):
    return templates.TemplateResponse(
        "Profil_Mahasiswa.html",
        {"request": request}
    )


# DASHBOARD ADMIN
@router.get("/admin/dashboard", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    return templates.TemplateResponse(
        "admin_dashboard.html",
        {"request": request}
    )