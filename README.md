# 🔬 Eksperimen_SML_AkbarNurRizqi

Repositori ini merupakan bagian dari submission proyek akhir kelas **Membangun Sistem Machine Learning - Dicoding**. Fokus dari repositori ini adalah pemenuhan **Kriteria 1** yaitu melakukan **eksperimen terhadap dataset pelatihan** menggunakan *template eksperimen MSML*, pembuatan preprocessing pipeline otomatis, dan implementasi workflow CI.

---

## 📊 1. Perkenalan Dataset

Dataset yang digunakan dalam proyek ini adalah **Telco Customer Churn** yang diperoleh dari platform Kaggle. Dataset ini berisi informasi mengenai pelanggan dari sebuah perusahaan telekomunikasi fiktif, dengan tujuan utama untuk memprediksi **kemungkinan pelanggan berhenti berlangganan (churn)** berdasarkan berbagai fitur seperti layanan yang digunakan, durasi langganan, dan biaya bulanan.

### 📑 Deskripsi Dataset

- **Jumlah data**: 7.043 entri (pelanggan)
- **Jumlah fitur**: 21 kolom, terdiri dari:
  - Fitur numerik: `tenure`, `MonthlyCharges`, `TotalCharges`
  - Fitur kategorikal: `gender`, `Partner`, `Dependents`, `PhoneService`, `InternetService`, dll.
  - Target: `Churn` (klasifikasi biner: `Yes`/`No`)

### 🎯 Tujuan Penggunaan Dataset

Dataset ini dipilih karena:

- Cocok untuk kasus **klasifikasi biner** (Churn atau Tidak)
- Memiliki kombinasi fitur **numerik dan kategorikal**
- Mendukung eksperimen preprocessing, pelatihan model, deployment, dan monitoring
- Sangat relevan untuk eksplorasi end-to-end **MLOps Workflow**

Dataset digunakan secara konsisten mulai dari:

- Eksplorasi dan preprocessing manual
- Automasi preprocessing (`automate_AkbarNurRizqi.py`)
- Pelatihan model MLflow
- CI/CD Workflow retraining otomatis
- Monitoring model (Prometheus & Grafana)

---

## 📁 2. Struktur Folder
Eksperimen_SML_AkbarNurRizqi/
├── .github/
│   └── workflows/
│       └── preprocess.yml              <- Workflow otomatisasi preprocessing (Advanced)
├── namadataset_raw/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── preprocessing/
│   ├── Eksperimen_AkbarNurRizqi.ipynb  <- Eksperimen manual menggunakan template MSML
│   ├── automate_AkbarNurRizqi.py       <- Script preprocessing otomatis (Skilled)
│   └── dataset_preprocessing/
│       ├── train.csv                   <- Hasil preprocessing (ready to train)
│       └── test.csv



## ✅ 3. Checklist Kriteria & Penilaian

### 🧪 Kriteria 1: Eksperimen terhadap Dataset Pelatihan — **✅ Advanced**

- Eksplorasi dan preprocessing data dilakukan **secara manual** menggunakan template MSML pada file notebook.
- Pipeline **automated preprocessing** dibangun dan dikonversi ke script Python (`automate_AkbarNurRizqi.py`)
- CI/CD preprocessing menggunakan **GitHub Actions** (`preprocess.yml`) secara otomatis menghasilkan dataset terbaru ketika ada perubahan di folder terkait.

---

## 🧰 Tools & Teknologi

| Tools            | Kegunaan                            |
| ---------------- | ----------------------------------- |
| Jupyter Notebook | Eksperimen & EDA                    |
| Python           | Automasi preprocessing              |
| Scikit-learn     | Encoding, scaling, train-test split |
| Pandas & NumPy   | Manipulasi data                     |
| GitHub Actions   | Workflow CI                         |

---

## 🏅 Hasil Penilaian Reviewer Dicoding

> ✅ **Kriteria 1: Melakukan Eksperimen Terhadap Dataset Pelatihan – ADVANCED**

> “Kriteria 1 berhasil dipenuhi secara **komprehensif** mulai dari eksplorasi manual, pembuatan pipeline preprocessing otomatis, hingga penerapan **workflow CI dengan GitHub Actions**. Repositori ini telah mencerminkan praktik terbaik dalam tahap awal sistem machine learning.”
