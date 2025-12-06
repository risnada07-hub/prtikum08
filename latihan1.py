class DaftarNilai:
    def __init__(self):
        # Struktur data: List of dictionaries
        # Setiap dictionary menyimpan {'nama': '...', 'nilai': ...}
        self.data_nilai = []

    # Method tambah() untuk menambah data mahasiswa
    def tambah(self, nama, nilai):
        """Menambah data mahasiswa baru."""
        # Validasi input nilai
        if not isinstance(nilai, (int, float)) or not (0 <= nilai <= 100):
             print(f" Nilai untuk {nama} tidak valid. Harus antara 0 dan 100.")
             return

        data_baru = {'nama': nama, 'nilai': nilai}
        self.data_nilai.append(data_baru)
        print(f" Data mahasiswa {nama} berhasil ditambahkan.")

    # Method tampilkan() untuk menampilkan semua data
    def tampilkan(self):
        """Menampilkan seluruh daftar nilai mahasiswa."""
        if not self.data_nilai:
            print(" Daftar nilai masih kosong.")
            return

        print("\n--- DAFTAR NILAI MAHASISWA ---")
        for i, data in enumerate(self.data_nilai, 1):
            print(f"{i}. Nama: {data['nama']}, Nilai: {data['nilai']}")
        print("------------------------------")

    # Method hapus(nama) untuk menghapus data berdasarkan nama
    def hapus(self, nama):
        """Menghapus data mahasiswa berdasarkan nama."""
        # Menggunakan list comprehension untuk membuat list baru
        # yang TIDAK mengandung data dengan nama yang dicari (case-insensitive)
        nama_ditemukan = any(data['nama'].lower() == nama.lower() for data in self.data_nilai)

        if nama_ditemukan:
            self.data_nilai = [data for data in self.data_nilai if data['nama'].lower() != nama.lower()]
            print(f" Data mahasiswa {nama} berhasil dihapus.")
        else:
            print(f" Data mahasiswa dengan nama {nama} tidak ditemukan.")

    # Method ubah(nama) untuk mengubah data berdasarkan nama
    def ubah(self, nama, nilai_baru):
        """Mengubah nilai mahasiswa berdasarkan nama."""
        # Cari data berdasarkan nama (case-insensitive)
        for data in self.data_nilai:
            if data['nama'].lower() == nama.lower():
                # Validasi input nilai baru
                if not isinstance(nilai_baru, (int, float)) or not (0 <= nilai_baru <= 100):
                     print(f" Nilai baru untuk {nama} tidak valid. Harus antara 0 dan 100.")
                     return

                data['nilai'] = nilai_baru
                print(f" Nilai mahasiswa {nama} berhasil diubah menjadi {nilai_baru}.")
                return # Keluar setelah berhasil diubah

        print(f" Data mahasiswa dengan nama {nama} tidak ditemukan.")


# --- Contoh Penggunaan Program ---
if __name__ == "__main__":
    # Inisialisasi objek (instance) dari class DaftarNilai
    manajemen_nilai = DaftarNilai()

    # 1. Menambah data
    print("\n--- Operasi Penambahan ---")
    manajemen_nilai.tambah("Budi", 85)
    manajemen_nilai.tambah("Ani", 92.5)
    manajemen_nilai.tambah("Citra", 78)
    manajemen_nilai.tambah("Dewi", 101) # Contoh data yang tidak valid

    # 2. Menampilkan data
    manajemen_nilai.tampilkan()

    # 3. Mengubah data
    print("\n--- Operasi Pengubahan ---")
    manajemen_nilai.ubah("budi", 90) # Ubah nama dengan case berbeda
    manajemen_nilai.ubah("Citra", 65)
    manajemen_nilai.ubah("Eko", 50) # Contoh nama tidak ditemukan

    # Tampilkan setelah diubah
    manajemen_nilai.tampilkan()

    # 4. Menghapus data
    print("\n--- Operasi Penghapusan ---")
    manajemen_nilai.hapus("Ani")
    manajemen_nilai.hapus("Fajar") # Contoh nama tidak ditemukan

    # Tampilkan setelah dihapus
    manajemen_nilai.tampilkan()