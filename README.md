# prtikum08
# Program Manajemen Nilai Mahasiswa Sederhana

**Tugas Praktikum:** Implementasi Class dalam Program Manajemen Nilai

## 1. Penjelasan Program

Program ini adalah sistem manajemen nilai mahasiswa sederhana yang diimplementasikan menggunakan konsep **Pemrograman Berorientasi Objek (PBO)** dalam bahasa Python. Program ini menggunakan sebuah `class` bernama `DaftarNilai` untuk mengelola data (menambah, menampilkan, menghapus, dan mengubah) nilai mahasiswa.

### Struktur Class: `DaftarNilai`

| Komponen | Deskripsi |
| :--- | :--- |
| **Atribut** | `self.data_nilai`: Sebuah list yang menyimpan data mahasiswa dalam bentuk *dictionary* (`{'nama': str, 'nilai': float/int}`). |
| **Method** | **`tambah(nama, nilai)`**: Menambahkan data mahasiswa baru. |
| | **`tampilkan()`**: Menampilkan seluruh data nama dan nilai yang tersimpan. |
| | **`hapus(nama)`**: Menghapus data mahasiswa berdasarkan input nama. |
| | **`ubah(nama, nilai_baru)`**: Mengubah nilai mahasiswa yang sudah ada berdasarkan input nama. |

## 2. Diagram Kelas (UML Sederhana)

Diagram kelas menunjukkan struktur *class* `DaftarNilai` secara visual:



| Class | Atribut | Methods |
| :--- | :--- | :--- |
| **DaftarNilai** | `- data_nilai: list` | `+ __init__()` |
| | | `+ tambah(nama: str, nilai: float/int)` |
| | | `+ tampilkan()` |
| | | `+ hapus(nama: str)` |
| | | `+ ubah(nama: str, nilai_baru: float/int)` |

## 3. Flowchart Program

Berikut adalah representasi visual dari alur program, dibagi menjadi Flowchart Utama (Menu) dan Flowchart Detail (Method `tambah`).



[Image of Flowchart Utama and Flowchart Detail for 'tambah' method.]


### 3.1 Flowchart Utama (Program Menu)

Menggambarkan alur eksekusi program dari awal hingga pemilihan operasi oleh pengguna.

1.  **Mulai:** Program dieksekusi.
2.  **Inisialisasi:** Objek `DaftarNilai` dibuat.
3.  **Loop Menu:** Program menampilkan menu opsi dan meminta input pilihan (1-5).
4.  **Keputusan Pilihan:**
    * **1-4:** Panggil method yang sesuai (`tambah`, `tampilkan`, `hapus`, atau `ubah`). Setelah selesai, kembali ke Menu.
    * **5 (Keluar):** Program dihentikan.
    * **Lainnya:** Tampilkan pesan error dan kembali ke Menu.
5.  **Selesai.**

### 3.2 Flowchart Detail (Method `tambah(nama, nilai)`)

Menggambarkan alur logika untuk penambahan data baru:

1.  **Mulai:** Method dipanggil dengan `nama` dan `nilai`.
2.  **Keputusan (Validasi):** Apakah nilai yang diinput valid (misalnya, $0 \le \text{nilai} \le 100$)?
    * **Ya:** Lanjut ke Proses.
    * **Tidak:** Langsung ke output error, dan Selesai.
3.  **Proses:** Data (nama dan nilai) dibuat dalam format *dictionary* dan ditambahkan ke list `data_nilai`.
4.  **Output:** Cetak pesan keberhasilan penambahan data.
5.  **Selesai.**

## 4. Cara Penggunaan (Asumsi Python)

1.  Simpan kode program dalam file `manajemen_nilai.py`.
2.  Jalankan program dari terminal:
    ```bash
    python manajemen_nilai.py
    ```
3.  Program akan menampilkan menu, dan Anda dapat memilih operasi (Tambah, Tampilkan, Hapus, Ubah) sesuai kebutuhan.
