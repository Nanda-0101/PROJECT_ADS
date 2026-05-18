from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import auth, admin, mahasiswa, tes

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Router
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(mahasiswa.router)
app.include_router(tes.router)