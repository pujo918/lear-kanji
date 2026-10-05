# 熟語マスター (Jukugo Master) 🎌

Aplikasi web interaktif untuk mempelajari kata majemuk kanji (**Jukugo / 熟語**) berdasarkan daftar kanji terorganisir per minggu (Minggu 1 s/d 6).

---

## 🌟 Fitur Utama

1. **Daftar Jukugo Lengkap (List View)**:
   - Menampilkan total **143 Kanji** dan **500 Jukugo berfrekuensi tinggi** (setiap kanji memiliki minimal 2 hingga maksimal 4 jukugo).
   - Dilengkapi **Furigana (Ruby)** di atas kanji yang bisa diatur: **Tampilkan Selalu** atau **Sembunyikan Furigana (Klik untuk Intip)** demi melatih daya ingat.
   - Arti lengkap dalam **Bahasa Indonesia** beserta romaji dan contoh kalimat kontekstual.
   - Tombol **Audio Pengucapan Bahasa Jepang** (Web Speech API native).
   - Filter berdasarkan **Minggu (Minggu 1 - 6)**, Filter **Kanji Tertentu**, Level JLPT, serta kotak pencarian kata kunci.

2. **🎴 Flashcard Mode (Front-Only / Tanpa Perlu Dibalik)**:
   - Sesuai dengan permintaan: kartu ditampilkan langsung satu sisi dengan kanji jukugo, furigana, dan arti bahasa Indonesia di bagian depan.
   - Tinggal klik tombol **"Berikutnya ➔"** atau **"⬅ Sebelumnya"** secara cepat.
   - **Shortcut Keyboard**:
     - Tombol `➔` (Panah Kanan) atau `Spasi`: Kartu Berikutnya
     - Tombol `⬅` (Panah Kiri): Kartu Sebelumnya
     - Tombol `S`: Dengarkan suara pelafalan Jepang
     - Tombol `F`: Simpan / Hapus Bintang Favorit
   - Fitur **Acak (Shuffle)** agar urutan tidak tertebak.
   - Fitur **Auto-Play (Slideshow 3s)** untuk belajar santai tanpa menyentuh layar.

3. **🎯 Latihan Soal Acak (Latsol / Kuis Interaktif)**:
   - 4 Pilihan Tipe Soal:
     1. **Tebak Furigana / Cara Baca (Hiragana)**
     2. **Tebak Arti Bahasa Indonesia**
     3. **Tebak Jukugo Kanji dari Arti**
     4. **Campuran Acak (Mixed Mode)**
   - Pilihan cakupan minggu (Semua Minggu atau per minggu).
   - Pilihan jumlah soal (10, 20, 30, atau 50 soal).
   - Umpan balik visual instan (Hijau = Benar, Merah = Salah) dengan kartu pembahasan contoh kalimat.
   - Efek suara sintetis (Web Audio API) untuk jawaban benar dan salah.
   - Halaman hasil evaluasi akhir dengan persentase nilai, grade (S/A/B/C/D), serta tombol **"Latihan Soal Salah Saja"** untuk memantapkan kata-kata yang sempat salah.

4. **⭐ Favorit & Bookmark**:
   - Beri bintang pada jukugo yang dirasa sulit untuk dipelajari tersendiri di halaman Favorit atau dibuka langsung ke mode Flashcard.

5. **🌓 Dark Mode & Light Mode**:
   - Tema elegan minimalis bernuansa khas Jepang dengan transisi halus dan tersimpan di penyimpanan lokal browser.

---

## 📂 Struktur File

```
jukugo-master/
├── index.html        # Antarmuka web utama (HTML5 semantik & responsif)
├── style.css         # Styling modern, tipografi Jepang Noto Sans JP, dark/light mode
├── data.js           # Database 143 Kanji & 500 Jukugo (Minggu 1 - 6)
├── app.js            # Logika filter, flashcard, TTS audio, kuis, dan local storage
├── build_data.py     # Script generator/verifikator data
└── README.md         # Dokumentasi penggunaan
```

---

## 🚀 Cara Menjalankan

### Cara 1: Buka Langsung (Tanpa Perlu Instalasi Apapun)
Cukup klik dua kali berkas `index.html` di penjelajah berkas Windows (File Explorer). Aplikasi akan langsung terbuka di browser seperti Google Chrome, Microsoft Edge, atau Mozilla Firefox.

### Cara 2: Melalui Local Web Server
Aplikasi saat ini telah aktif di:
👉 **[http://localhost:8080](http://localhost:8080)**

Jika ingin menjalankan server kembali di kemudian hari, jalankan perintah berikut di PowerShell atau Command Prompt pada folder proyek:
```powershell
python -m http.server 8080
```
Lalu buka peramban web ke `http://localhost:8080`.
