# SIPEKA - Sistem Prediksi Kepribadian Mahasiswa

:contentReference[oaicite:0]{index=0}

SIPEKA adalah aplikasi berbasis web untuk memprediksi kepribadian mahasiswa (Introvert, Ekstrovert, Ambivert) menggunakan pendekatan **Machine Learning Ensemble** yang terdiri dari:

- XGBoost
- LightGBM
- Neural Network

Sistem dibangun menggunakan **FastAPI** sebagai backend, **MySQL** sebagai database, serta integrasi model AI melalui **Hugging Face Spaces**.

---

## 🚀 Fitur Utama

### 👨‍🎓 Mahasiswa
- Login pengguna
- Mengisi tes kepribadian (93 pertanyaan)
- Melihat hasil prediksi kepribadian
- Riwayat hasil tes
- Edit profil
- Logout

### 🧑‍💼 Admin
- Login admin
- Manajemen data mahasiswa
- Manajemen admin
- Monitoring seluruh hasil tes
- Statistik hasil prediksi
- Edit profil admin
- Logout

---

## ⚙️ Teknologi yang Digunakan

- Python 3.11
- FastAPI
- MySQL / MariaDB (XAMPP)
- SQLAlchemy
- PyMySQL
- Machine Learning (XGBoost, LightGBM, Neural Network)
- Hugging Face Inference API
- Uvicorn

---

## 📥 Instalasi & Setup Project

### 1. Clone Repository

```bash
git clone https://github.com/Nanda-0101/PROJECT_ADS.git
cd PROJECT_ADS
```

---

### 2. Buat Virtual Environment

```bash
python -m venv ads
```

Aktifkan environment:

**Windows (PowerShell):**
```bash
ads\Scripts\Activate.ps1
```

**Windows (CMD):**
```bash
ads\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Setup Database MySQL

### 4.1 Buat Database

Jalankan perintah berikut di MySQL / phpMyAdmin:

```sql
CREATE DATABASE database;
```

---

### 4.2 Import Struktur Database

Import file `database.sql` yang tersedia di repository:

Langkah:
- Buka phpMyAdmin
- Pilih database `database`
- Klik tab **Import**
- Upload file `database.sql`
- Klik **Go**

---

## 🔐 Konfigurasi Environment (.env)

Buat file `.env` di root project:

```env
DATABASE_URL=mysql+pymysql://root:@localhost:3306/database
```

Jika MySQL menggunakan password:

```env
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/database
```

📌 Catatan penting:
- File `.env` tidak disimpan di GitHub
- Wajib dibuat manual sebelum menjalankan aplikasi

---

## ▶️ Menjalankan Aplikasi

Masuk ke folder aplikasi:

```bash
cd app
```

Jalankan server FastAPI:

```bash
uvicorn main:app --reload
```

Akses aplikasi di browser:

```
http://127.0.0.1:8000
```

---

## 🧠 Arsitektur Sistem

### 📁 Backend (FastAPI)

Struktur utama project:

```
app/
│── main.py              # Entry point aplikasi
│
├── routers/            # API endpoint
│   ├── auth.py
│   ├── mahasiswa.py
│   ├── admin.py
│   └── tes.py
│
├── models/             # Database model (SQLAlchemy)
├── services/           # Integrasi ML (Hugging Face)
├── core/               # Config database & security
└── utils/              # Helper function
```

---

## 🤖 Machine Learning System

SIPEKA menggunakan pendekatan **ensemble learning**, yaitu:

- XGBoost → model boosting
- LightGBM → gradient boosting framework
- Neural Network → deep learning model

### 🔄 Metode Prediksi
Hasil akhir ditentukan menggunakan:

```
Weighted Ensemble Voting
```

Setiap model memberikan probabilitas, kemudian digabungkan untuk menentukan kelas akhir:

- Introvert
- Ekstrovert
- Ambivert

---

## 🌐 Integrasi Hugging Face

Model tidak disimpan di GitHub, tetapi di-deploy di Hugging Face Space.

File utama:
```
huggingface_service.py
```

Fungsi:
- Mengirim data jawaban ke API `/predict`
- Menerima hasil prediksi
- Mengembalikan probabilitas + label kepribadian

---

## 📊 Database & Relasi

Tabel utama:
- users
- mahasiswa
- admin
- tes
- hasil_tes

Relasi:
- User → Mahasiswa/Admin
- Mahasiswa → Tes
- Tes → Hasil Prediksi

---

## 📌 Troubleshooting

### ❌ Error: Database Connection Failed
- Pastikan MySQL aktif (XAMPP)
- Cek `.env`
- Pastikan database sudah dibuat

---

### ❌ Module Not Found
```bash
pip install -r requirements.txt
```

---

### ❌ Uvicorn Tidak Jalan
```bash
pip install uvicorn
```

---

### ❌ Port Sudah Dipakai
```bash
uvicorn main:app --port 8001 --reload
```

---

## 🧪 Testing Aplikasi

- Login sebagai mahasiswa
- Isi tes 93 soal
- Submit hasil
- Cek hasil prediksi
- Login admin untuk melihat statistik

---

## 👨‍💻 Pengembang

Proyek ini dikembangkan untuk tugas **Analisis Data System (ADS)** dengan integrasi:

- FastAPI Backend
- MySQL Database
- Machine Learning Ensemble
- Hugging Face Deployment

---

## 📌 Catatan Penting

- Pastikan Python **3.11**
- Wajib install `requirements.txt`
- Database harus di-import sebelum run
- `.env` wajib dibuat manual
- Model ML tidak disimpan di GitHub

---
