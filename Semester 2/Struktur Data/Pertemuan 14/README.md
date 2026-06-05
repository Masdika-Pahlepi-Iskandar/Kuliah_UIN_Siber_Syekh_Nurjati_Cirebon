
Project ini merupakan Sistem Antrian STNK Samsat Berbasis Web yang dirancang untuk membantu proses pelayanan administrasi kendaraan di Samsat menjadi lebih terorganisir, efisien, dan mudah dikelola. Sistem ini memanfaatkan metode FIFO (First In First Out), yaitu pelanggan yang datang lebih dahulu akan mendapatkan pelayanan lebih dahulu sesuai urutan antreannya.

Pada sistem ini, masyarakat dapat melakukan pendaftaran antrean dengan memasukkan data diri, nomor polisi kendaraan, serta jenis layanan yang dibutuhkan. Setelah pendaftaran berhasil, sistem secara otomatis akan memberikan nomor antrean dan menentukan loket pelayanan yang sesuai dengan jenis layanan yang dipilih.

Sistem mendukung lima loket pelayanan, yaitu Perpanjangan STNK Tahunan, Perpanjangan STNK 5 Tahunan, Balik Nama Kendaraan, Ganti STNK Hilang atau Rusak, dan Mutasi Kendaraan. Setiap loket memiliki antrean tersendiri sehingga proses pelayanan dapat berjalan lebih cepat dan terstruktur.

Selain mengelola antrean, sistem juga menyediakan fitur pemanggilan pelanggan secara otomatis, pencatatan riwayat pelayanan, monitoring statistik pelayanan secara real-time, serta notifikasi suara menggunakan teknologi Text-to-Speech (gTTS). Dengan fitur tersebut, petugas dapat memantau kondisi pelayanan dengan mudah, sementara masyarakat dapat memperoleh informasi antrean secara jelas dan transparan.

Project ini dibangun menggunakan FastAPI sebagai backend untuk mengelola logika sistem dan layanan API, serta Streamlit sebagai frontend untuk menampilkan antarmuka pengguna yang interaktif. Melalui penerapan teknologi tersebut, sistem mampu memberikan solusi digital dalam pengelolaan antrean pelayanan Samsat sehingga meningkatkan kualitas pelayanan publik dan mengurangi risiko kesalahan dalam proses antrean.


# 🚗 Sistem Antrian STNK Samsat

Aplikasi sistem antrian digital untuk pelayanan STNK Samsat berbasis **FastAPI** (backend) dan **Streamlit** (frontend), dengan dukungan Text-to-Speech (TTS) menggunakan **gTTS**.

---

## 📁 Struktur Proyek

```
.
├── backend.py      # API server (FastAPI) — logika antrian FIFO multi-loket + TTS
└── frontend.py     # Tampilan UI (Streamlit) — dashboard antrian real-time
```

---

## ⚙️ Persyaratan Sistem

- Python **3.8+**
- pip

### Instalasi Dependensi

```bash
# Backend
pip install fastapi uvicorn gtts

# Frontend
pip install streamlit requests
```

---

## 🚀 Cara Menjalankan

> Backend **harus** dijalankan terlebih dahulu sebelum frontend.

### 1. Jalankan Backend

```bash
python -m uvicorn backend:app --reload --port 8000
```

Backend akan berjalan di: `http://localhost:8000`

### 2. Jalankan Frontend

```bash
streamlit run frontend.py
```

Frontend akan terbuka otomatis di browser (default: `http://localhost:8501`)

---

## 🏛️ Arsitektur

```
┌─────────────────┐        HTTP/REST        ┌──────────────────────┐
│  frontend.py    │ ──────────────────────► │  backend.py          │
│  (Streamlit)    │ ◄────────────────────── │  (FastAPI :8000)     │
│                 │    JSON + Audio URL      │                      │
│  • Form daftar  │                          │  • Antrian FIFO      │
│  • Loket view   │                          │  • Multi-loket (1–5) │
│  • Riwayat      │                          │  • TTS (gTTS)        │
│  • Audio TTS    │                          │  • REST Endpoints    │
└─────────────────┘                          └──────────────────────┘
```

---

## 🗂️ Loket & Jenis Layanan

| Loket | Prefix | Jenis Layanan                   |
|-------|--------|----------------------------------|
| 1     | A      | Perpanjangan STNK Tahunan        |
| 2     | B      | Perpanjangan STNK 5 Tahunan      |
| 3     | C      | Balik Nama Kendaraan             |
| 4     | D      | Ganti STNK Hilang/Rusak          |
| 5     | E      | Mutasi Kendaraan                 |

Format nomor antrian: `[Prefix][001–999]` — contoh: `A001`, `B023`, `E005`

---

## 📡 API Endpoints (Backend)

| Method | Endpoint           | Deskripsi                                  |
|--------|--------------------|--------------------------------------------|
| GET    | `/info`            | Status & jam pelayanan saat ini            |
| GET    | `/state`           | State lengkap semua loket + statistik      |
| GET    | `/layanan`         | Daftar jenis layanan & peta loket          |
| POST   | `/daftar`          | Daftarkan pelanggan baru ke antrian        |
| POST   | `/panggil/{loket}` | Panggil nomor antrian berikutnya           |
| POST   | `/selesai/{loket}` | Tandai pelayanan loket selesai             |
| POST   | `/reset`           | Reset seluruh sistem antrian               |
| GET    | `/audio/{nama}`    | Unduh/stream file audio TTS (.mp3)         |

### Contoh Request `/daftar`

```json
POST /daftar
{
  "nama": "Budi Santoso",
  "no_polisi": "B 1234 ABC",
  "jenis_layanan": "Perpanjangan STNK Tahunan",
  "no_hp": "08123456789"
}
```

### Contoh Response `/daftar`

```json
{
  "nomor": "A001",
  "loket": 1,
  "estimasi": 10,
  "audio": "daftar_A001",
  "pesan": "Berhasil! Nomor antrian: A001 — Loket 1"
}
```

---

## 🖥️ Fitur Frontend

- **Sidebar** — Form pendaftaran antrian (nama, nomor polisi, jenis layanan, nomor HP)
- **Kolom Kiri** — Statistik ringkasan: menunggu, sedang dilayani, selesai
- **Kolom Tengah** — Status real-time per loket, tombol Panggil & Selesai, daftar tunggu
- **Kolom Kanan** — Riwayat pelayanan per loket, info jam & hari pelayanan, info nomor loket, indikator kapasitas
- **Audio TTS** — Pengumuman suara otomatis dalam Bahasa Indonesia saat daftar, panggil, dan selesai

---

## 🔊 Text-to-Speech (TTS)

Audio dihasilkan secara otomatis menggunakan **gTTS** (Google Text-to-Speech) dalam Bahasa Indonesia untuk tiga momen:

| Momen     | Contoh Pesan                                                                 |
|-----------|------------------------------------------------------------------------------|
| Daftar    | "Selamat datang, Budi. Nomor antrian Anda adalah A001, untuk loket 1..."     |
| Panggil   | "Perhatian. Nomor antrian A001, atas nama Budi, dimohon segera menuju loket 1..." |
| Selesai   | "Pelayanan atas nama Budi di loket 1 telah selesai. Terima kasih..."         |

File audio disimpan sementara di direktori `tempfile.gettempdir()` dan diakses melalui endpoint `/audio/{nama_file}`.

> Jika gTTS gagal (misal: tidak ada koneksi internet), sistem tetap berjalan tanpa audio.

---

## ⏰ Jam & Hari Pelayanan

| Keterangan | Nilai                  |
|------------|------------------------|
| Hari aktif | Senin – Jumat          |
| Jam buka   | 08:00 WIB              |
| Jam tutup  | 16:00 WIB              |
| Hari libur | Sabtu & Minggu         |

> Catatan: Validasi jam pelayanan di backend saat ini dikonfigurasi selalu aktif (`cek_jam_pelayanan` mengembalikan `True`). Untuk mengaktifkan pembatasan jam, sesuaikan fungsi tersebut di `backend.py`.

---

## 🧠 Struktur Data

Backend menggunakan implementasi **FIFO (First In, First Out)** secara manual menggunakan *linked list* (`Node` + `AntrianFIFO`), bukan `collections.deque`, untuk keperluan edukasi dan transparansi algoritma.

```
Antrian FIFO:
  enqueue() → tambah ke belakang
  dequeue() → ambil dari depan
  peek()    → lihat depan tanpa menghapus
```

---

## 🔧 Konfigurasi

Ubah nilai berikut di `frontend.py` jika backend berjalan di host/port berbeda:

```python
BASE_URL = "http://localhost:8000"
```

---

## 📝 Lisensi

Proyek ini dibuat untuk keperluan edukasi dan simulasi sistem antrian pelayanan publik.
