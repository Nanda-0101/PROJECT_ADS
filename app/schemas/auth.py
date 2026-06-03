from pydantic import BaseModel

class LoginRequest(BaseModel):
    nim: str | None = None
    username: str | None = None
    password: str
    role: str  # 'mahasiswa' or 'admin'

class LoginResponse(BaseModel):
    success: bool
    role: str | None = None
    nama: str | None = None
    user_id: int | None = None
    redirect_url: str | None = None
    message: str | None = None