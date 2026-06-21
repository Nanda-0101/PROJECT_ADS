# 1. SIPEKA Sistem Prediksi Kepribadian Mahasiswa

<p align="center">
  <b>Sistem Prediksi Kepribadian Mahasiswa</b><br>
  Introvert • Ekstrovert • Ambivert Klasifikasi Menggunakan Machine Learning Ensemble
</p>

---

## 2. Repository
https://github.com/Nanda-0101/PROJECT_ADS

---

## 3. Overview

**SIPEKA** adalah sistem berbasis web yang digunakan untuk memprediksi kepribadian mahasiswa menggunakan pendekatan **Artificial Intelligence & Machine Learning Ensemble**.

Sistem ini menggabungkan:
- XGBoost
- LightGBM
- Neural Network

dengan backend **FastAPI**, database **MySQL**, serta frontend **Vanilla JavaScript (HTML + CSS + JS)**.

---

## 4. Key Features

### Mahasiswa
- Login & autentikasi
- Tes kepribadian (93 pertanyaan)
- Hasil prediksi otomatis
- Riwayat tes
- Edit profil
- Logout

### Admin Panel
- Admin authentication
- Manajemen mahasiswa
- Manajemen admin
- Statistik hasil tes
- Monitoring data prediksi
- Profil admin management

---

## 5. Machine Learning Architecture

### Model Output
- Introvert
- Ekstrovert
- Ambivert

---

## 6. Tech Stack

| Layer | Technology |
|------|------------|
| Backend | FastAPI |
| Frontend | HTML + CSS + Vanilla JavaScript |
| UI Styling | Bootstrap 3 + Custom CSS |
| Database | MySQL |
| ORM | SQLAlchemy |
| ML Models | XGBoost • LightGBM • Neural Network |
| API ML | Hugging Face Spaces |
| Server | Uvicorn |

---

## 7. Frontend (Vanilla JS Architecture)

Frontend SIPEKA dibangun menggunakan **template engine FastAPI (Jinja2-like HTML rendering)** dan **Vanilla JavaScript tanpa framework**.

### Struktur Frontend

```
static/
│
├── assets/          # gambar UI (dashboard, logo, banner, dll)
├── css/             # styling custom
│   ├── style.css
│   ├── style_admin.css
│   ├── DashMhs.css
│   └── ...
├── js/              # vanilla JavaScript logic
│   ├── script.js
│   └── script_admin.js
```

---

### Templates (UI Pages)

```
templates/
│
├── login.html
├── DashMhs.html
├── Tes_Mahasiswa.html
├── RiwayatTesMhs.html
├── Profil_Mahasiswa.html
│
├── admin_dashboard.html
├── admin_KelolaMahasiswa.html
├── admin_KelolaAdmin.html
├── admin_RiwayatTesMahasiswa.html
└── Profil_Admin.html
```

---

### Frontend Flow (Vanilla JS)

1. User login melalui `login.html`
2. JavaScript mengirim request ke FastAPI backend
3. Backend mengembalikan session/cookie login
4. User diarahkan ke dashboard:
   - Mahasiswa → `DashMhs.html`
   - Admin → `admin_dashboard.html`
5. JS menangani:
   - Submit tes (AJAX/fetch)
   - Validasi form
   - Render hasil prediksi
   - Load riwayat data secara dinamis

---

## 8. Installation Guide

### 8.1 Clone Repository
```bash
git clone https://github.com/Nanda-0101/PROJECT_ADS.git
cd PROJECT_ADS
```

---

### 8.2 Create Virtual Environment
```bash
python -m venv ads
```

Activate:
```bash
ads\Scripts\Activate.ps1
```

---

### 8.3 Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 9. Database Setup

### 9.1 Create Database
```sql
CREATE DATABASE database;
```

---

### 9.2 Import SQL File
- Buka phpMyAdmin
- Pilih database `database`
- Import file `database.sql`

---

## 10. Environment Configuration

Buat file `.env`:

```env
DATABASE_URL=mysql+pymysql://root:@localhost:3306/database
```

Jika ada password:

```env
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/database
```

---

## 11. Run Application

```bash
cd app
uvicorn main:app --reload
```

Akses aplikasi:
```
http://127.0.0.1:8000
```

---

## 12. Project Structure

```
app/
│
├── main.py
│
├── core/
├── models/
├── routers/
├── services/
│
├── static/        # Vanilla JS frontend assets
├── templates/     # HTML UI pages
│
└── utils/
```

---

## 13. AI Integration (Hugging Face)

Endpoint:
```
/predict
```

File:
```
huggingface_service.py
```

Fungsi:
- Mengirim jawaban mahasiswa
- Menerima hasil prediksi
- Mengembalikan probabilitas + label

---

## 14. Database Schema

- users
- mahasiswa
- admin
- tes
- hasil_tes

Relasi:
```
Mahasiswa → Tes → Hasil Prediksi
```

---

## 15. Common Issues

### ❌ Database Error
- Pastikan MySQL aktif
- Cek `.env`

---

### ❌ Module Not Found
```bash
pip install -r requirements.txt
```

---

### ❌ Uvicorn Error
```bash
pip install uvicorn
```

---

### ❌ Port Conflict
```bash
uvicorn main:app --port 8001 --reload
```

---

## 16. System Workflow

1. Login mahasiswa / admin
2. Load UI (HTML + CSS)
3. Interaksi user via Vanilla JS
4. Request ke FastAPI backend
5. ML model memproses data
6. Hasil dikembalikan ke frontend
7. UI update secara dinamis

---

## 17. Notes

✔ Python 3.11 wajib  
✔ Database harus di-import dulu  
✔ Frontend menggunakan Vanilla JS (tanpa framework)  
✔ Assets berada di folder `static/`  
✔ Template UI berada di folder `templates/`  
✔ `.env` wajib dibuat manual  

---

<p align="center">
  <b>SIPEKA - AI Personality Prediction System</b><br>
  Built with FastAPI • Vanilla JS • MySQL • Machine Learning
</p>
