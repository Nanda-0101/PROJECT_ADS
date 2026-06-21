# 1. SIPEKA - Sistem Prediksi Kepribadian Mahasiswa

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql" />
  <img src="https://img.shields.io/badge/ML-Ensemble-red?style=for-the-badge&logo=tensorflow" />
</p>

<p align="center">
  <b>AI-Based Personality Prediction System for Students</b><br>
  Introvert • Ekstrovert • Ambivert Classification using Machine Learning Ensemble
</p>

---

## 2. Repository
👉 https://github.com/Nanda-0101/PROJECT_ADS

---

## 3. Overview

**SIPEKA** adalah sistem berbasis web yang digunakan untuk memprediksi kepribadian mahasiswa menggunakan pendekatan **Artificial Intelligence & Machine Learning Ensemble**.

Sistem ini menggabungkan:
- XGBoost
- LightGBM
- Neural Network

dengan backend **FastAPI** dan database **MySQL**.

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

## (Dihapus sesuai permintaan - flowchart tidak ditampilkan)

### Model Output
- Introvert
- Ekstrovert
- Ambivert

---

## 6. Tech Stack

| Layer | Technology |
|------|------------|
| Backend | FastAPI |
| Database | MySQL |
| ORM | SQLAlchemy |
| ML Models | XGBoost • LightGBM • Neural Network |
| API ML | Hugging Face Spaces |
| Server | Uvicorn |

---

## 7. Installation Guide

### 7.1 Clone Repository
```bash
git clone https://github.com/Nanda-0101/PROJECT_ADS.git
cd PROJECT_ADS
```

---

### 7.2 Create Virtual Environment
```bash
python -m venv ads
```

Activate:
```bash
ads\Scripts\Activate.ps1
```

---

### 7.3 Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 8. Database Setup

### 8.1 Create Database
```sql
CREATE DATABASE database;
```

---

### 8.2 Import SQL File
- Buka phpMyAdmin
- Pilih database `database`
- Import file `database.sql`

---

## 9. Environment Configuration

Buat file `.env`:

```env
DATABASE_URL=mysql+pymysql://root:@localhost:3306/database
```

Jika ada password:

```env
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/database
```

⚠️ File `.env` wajib dibuat manual (tidak ada di GitHub)

---

## 10. Run Application

```bash
cd app
uvicorn main:app --reload
```

Akses aplikasi:
```
http://127.0.0.1:8000
```

---

## 11. Project Structure

```
app/
│
├── main.py
├── routers/
│   ├── auth.py
│   ├── admin.py
│   ├── mahasiswa.py
│   └── tes.py
│
├── models/
├── services/
├── core/
└── utils/
```

---

## 12. AI Integration (Hugging Face)

Model di-deploy di Hugging Face Space.

Endpoint:
```
/predict
```

File utama:
```
huggingface_service.py
```

Fungsi:
- Mengirim jawaban mahasiswa
- Menerima hasil prediksi
- Mengembalikan probabilitas + label

---

## 13. Database Schema

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

## 14. Common Issues

### ❌ Database Error
- Pastikan MySQL aktif
- Cek file `.env`

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

## 15. System Workflow

1. Login mahasiswa
2. Isi 93 pertanyaan
3. Data dikirim ke ML API
4. Ensemble model memproses
5. Hasil ditampilkan
6. Admin memonitor hasil

---


## 16. Notes

✔ Python 3.11 wajib  
✔ Database harus di-import dulu  
✔ `.env` dibuat manual  
✔ Model tidak disimpan di GitHub (Hugging Face only)

---

<p align="center">
  <b>SIPEKA - AI Personality Prediction System</b><br>
  Built with FastAPI • MySQL • Machine Learning
</p>
