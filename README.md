# 🎯 SIPEKA - Sistem Prediksi Kepribadian Mahasiswa

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

## 🌐 Repository
👉 :contentReference[oaicite:0]{index=0}

---

## ✨ Overview

**SIPEKA** adalah sistem berbasis web yang digunakan untuk memprediksi kepribadian mahasiswa menggunakan pendekatan **Artificial Intelligence & Machine Learning Ensemble**.

Sistem ini menggabungkan:
- XGBoost
- LightGBM
- Neural Network

dengan backend **FastAPI** dan database **MySQL**.

---

## 🚀 Key Features

### 👨‍🎓 Mahasiswa
- 🔐 Login & autentikasi
- 📝 Tes kepribadian (93 pertanyaan)
- 📊 Hasil prediksi otomatis
- 📚 Riwayat tes
- 👤 Edit profil
- 🚪 Logout

### 🧑‍💼 Admin Panel
- 🔐 Admin authentication
- 👥 Manajemen mahasiswa
- 🛠️ Manajemen admin
- 📊 Statistik hasil tes
- 📈 Monitoring data prediksi
- ⚙️ Profil admin management

---

## 🧠 Machine Learning Architecture

```mermaid
graph TD
A[Jawaban Mahasiswa] --> B[Preprocessing]
B --> C1[XGBoost Model]
B --> C2[LightGBM Model]
B --> C3[Neural Network]
C1 --> D[Weighted Voting Ensemble]
C2 --> D
C3 --> D
D --> E[Output: Personality Prediction]
```

### 🔬 Model Output
- Introvert
- Ekstrovert
- Ambivert

---

## 🏗️ Tech Stack

| Layer | Technology |
|------|------------|
| Backend | FastAPI ⚡ |
| Database | MySQL 🗄️ |
| ORM | SQLAlchemy |
| ML Models | XGBoost • LightGBM • Neural Network |
| API ML | Hugging Face Spaces 🤗 |
| Server | Uvicorn |

---

## 📦 Installation Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Nanda-0101/PROJECT_ADS.git
cd PROJECT_ADS
```

---

### 2️⃣ Create Virtual Environment
```bash
python -m venv ads
```

Activate:
```bash
ads\Scripts\Activate.ps1
```

---

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

### 4️⃣ Create Database
```sql
CREATE DATABASE database;
```

### 5️⃣ Import SQL File
- Open phpMyAdmin
- Select database `database`
- Import `database.sql`

---

## 🔐 Environment Configuration

Create file `.env`:

```env
DATABASE_URL=mysql+pymysql://root:@localhost:3306/database
```

If password exists:
```env
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/database
```

⚠️ `.env` is NOT included in repository (must be created manually)

---

## ▶️ Run Application

```bash
cd app
uvicorn main:app --reload
```

🌍 Open in browser:
```
http://127.0.0.1:8000
```

---

## 🧩 Project Structure

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
├── services/      # ML + Hugging Face API
├── core/          # DB config & security
└── utils/
```

---

## 🤖 AI Integration (Hugging Face)

📌 Model deployed on Hugging Face Space  
📡 Communication via API:

```
/predict
```

File:
```
huggingface_service.py
```

Function:
- Send user answers
- Receive probability scores
- Return final classification

---

## 📊 Database Schema

- users
- mahasiswa
- admin
- tes
- hasil_tes

Relasi utama:
```
Mahasiswa → Tes → Hasil Prediksi
```

---

## ⚠️ Common Issues

### ❌ Database Error
✔ Pastikan MySQL running  
✔ Cek `.env`  

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

## 📌 System Workflow

1. Login mahasiswa
2. Isi 93 pertanyaan
3. Data dikirim ke ML API
4. Ensemble model memproses
5. Hasil ditampilkan ke user
6. Admin memonitor hasil

---

## 👨‍💻 Developer

Project ini dikembangkan untuk tugas **Analisis Data System (ADS)** dengan integrasi:

- ⚡ FastAPI Backend
- 🗄️ MySQL Database
- 🤖 Machine Learning Ensemble
- ☁️ Hugging Face Deployment

---

## 📌 Future Improvements

- 📊 Dashboard analytics interaktif
- 📄 Export PDF hasil tes
- 🔐 Role-based access control (RBAC)
- ☁️ Deployment VPS / Docker
- 📡 REST API documentation (Swagger enhancement)

---

## 🎯 Notes

✔ Python 3.11 required  
✔ Database must be imported first  
✔ `.env` wajib dibuat manual  
✔ Model tidak disimpan di GitHub (Hugging Face only)

---

<p align="center">
  <b>🚀 SIPEKA - AI Personality Prediction System</b><br>
  Built with FastAPI • MySQL • Machine Learning
</p>
