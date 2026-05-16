from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_303_SEE_OTHER

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# (MENAMPILKAN LOGIN MAHASISWA)
@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        "login_mahasiswa.html",
        {"request": request}
    )

@app.post("/login")
async def handle_login(nim: str = Form(...), password: str = Form(...)):
    # Akun sementara untuk uji coba
    if nim == "admin" and password == "rahasia": 
        # Jika sesuai,  pindah ke dashboard admin
        return RedirectResponse(url="/admin-dashboard", status_code=HTTP_303_SEE_OTHER)
    
    # Jika gagal, kembalikan ke halaman login awal
    return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)

# MENAMPILKAN HALAMAN DASHBOARD ADMIN
@app.get("/admin-dashboard", response_class=HTMLResponse)
async def show_dashboard(request: Request):
    return templates.TemplateResponse(
        "admin_dashboard.html", 
        {"request": request}
    )
