from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.core.database import Base, engine

# Import model agar tabel terbentuk
from app.models import mahasiswa
from app.models import admin

# Import router
from app.routers.router import router as main_router
from app.routers.mahasiswa_router import router as mahasiswa_router
from app.routers.kelola_admin import router as kelola_admin_router


# =========================
# CREATE DATABASE TABLES
# =========================
Base.metadata.create_all(bind=engine)


# =========================
# FASTAPI APP
# =========================
app = FastAPI(
    title="SIPEKA - Sistem Informasi Kepribadian",
    version="1.0.0"
)


# =========================
# REGISTER ROUTERS
# =========================
app.include_router(main_router)
app.include_router(mahasiswa_router)
app.include_router(kelola_admin_router)


# =========================
# STATIC FILES
# =========================
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


# =========================
# HEALTH CHECK
# =========================
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }