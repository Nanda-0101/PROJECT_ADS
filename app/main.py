from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import router
from app.core.database import engine, Base
from app.models import mahasiswa, admin  # Import models

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SIPEKA - Sistem Informasi Kepribadian")

# Include routers
app.include_router(router.router)

# Include routers
app.include_router(router.router)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/health")
def health_check():
    return {"status": "healthy"}
