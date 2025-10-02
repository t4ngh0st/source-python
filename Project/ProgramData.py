data_siswa = []  # untuk menampung semua yang diinput user

def display_menu():
    """Menampilkan opsi menu utama."""
    print("\n============ MENU ============")
    print("1. Input Data Siswa")
    print("2. Jumlah Data Siswa")
    print("3. Pencarian Data Siswa")
    print("4. Pengurutan Data Siswa")
    print("5. Cetak Data Siswa")
    print("6. Exit")
    print("==============================")

def get_menu_choice():
    """Mendapatkan dan memvalidasi pilihan menu pengguna."""
    while True:
        try:
            pilihan = int(input("Pilih menu [1-6] : "))
            if 1 <= pilihan <= 6:
                return pilihan
            else:
                print("Pilihan tidak valid. Masukkan angka antara 1-6.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

def input_student_data():
    """Memasukkan data untuk siswa baru dan menambahkannya ke daftar global."""
    global data_siswa
    print("\n--- Input Data Siswa ---")
    nama = input("Masukkan Nama Siswa : ").strip()
    jurusan = input("Masukan Jurusan : ").strip()
    while True:
        kelas_str = input("Kelas (angka, misal: 10, 11, 12) : ").strip()
        try:
            kelas = int(kelas_str)
            break
        except ValueError:
            print("Kelas harus berupa angka. Silakan coba lagi.")
    
    data_siswa.append({"nama": nama, "jurusan": jurusan, "kelas": kelas})
    print("=" * 50)
    print("--- Data Siswa Berhasil Di Input! ---")
    print("=" * 50)

def display_student_count():
    """Menampilkan jumlah total siswa."""
    global data_siswa
    print("\n--- Jumlah Data Siswa ---")
    jumlah_siswa = len(data_siswa)
    print(f"Jumlah Siswa: {jumlah_siswa}")
    print("=" * 50)

def _print_student_details(siswa):
    """Fungsi bantuan untuk mencetak detail satu siswa."""
    print(f"Nama        : {siswa['nama']}")
    print(f"Jurusan     : {siswa['jurusan']}")
    print(f"Kelas       : {siswa['kelas']}")

def search_student_data():
    """Mencari siswa berdasarkan nama."""
    global data_siswa
    print("\n--- Pencarian Data Siswa ---")
    if not data_siswa:
        print("Belum ada data siswa untuk dicari.")
        print("=" * 50)
        return

    nama_cari = input("Masukkan Nama Siswa Yang Dicari : ").strip().lower()
    ditemukan = False
    for siswa in data_siswa:
        if siswa["nama"].lower() == nama_cari:
            print("=" * 50)
            print("Data siswa ditemukan:")
            _print_student_details(siswa)
            print("=" * 50)
            ditemukan = True
            break 
    
    if not ditemukan:
        print("\n=================================")
        print("--- Data Siswa Tidak Ditemukan ---")
        print("=================================\n")

def sort_student_data():
    """Mengurutkan data siswa berdasarkan nama atau kelas."""
    global data_siswa
    print("\n--- Pengurutan Data Siswa ---")
    if not data_siswa:
        print("Belum ada data siswa untuk diurutkan.")
        print("=" * 50)
        return

    print("Pilihan Pengurutan Data:")
    print("1. Berdasarkan Nama (A-Z)")
    print("2. Berdasarkan Kelas (Terkecil-Terbesar)")

    while True:
        pilihan_urut = input("Pilih cara pengurutan [1-2]: ").strip()
        if pilihan_urut == "1":
            data_siswa.sort(key=lambda m: m["nama"].lower())
            print("\nData Siswa berhasil diurutkan berdasarkan Nama.")
            break
        elif pilihan_urut == "2":
            data_siswa.sort(key=lambda m: m["kelas"]) # 'kelas' sudah int
            print("\nData Siswa berhasil diurutkan berdasarkan Kelas (terkecil).")
            break
        else:
            print("Pilihan pengurutan tidak valid. Silakan pilih 1 atau 2.")
    
    print_all_students(header="--- Data Siswa Terurut ---", show_empty_message=False)

def print_all_students(header="--- Data Semua Siswa ---", show_empty_message=True):
    """Mencetak semua data siswa."""
    global data_siswa
    print(f"\n{header}")
    if not data_siswa:
        if show_empty_message:
            print("Belum ada data siswa untuk dicetak.")
        print("=" * 50)
        return

    for siswa in data_siswa:
        _print_student_details(siswa)
        print("-" * 30) # Pemisah antar entri siswa
    print("=" * 50)


def ask_to_continue():
    """Menanyakan kepada pengguna apakah ingin kembali ke menu utama.
    Mengembalikan True untuk melanjutkan, False untuk keluar dari program."""
    while True:
        print("") # Tambahkan baris kosong untuk spasi
        ulang = input("Apakah Anda ingin kembali ke Menu Utama? [y/n] : ").strip().lower()
        if ulang == "y":
            return True
        elif ulang == "n":
            print("\n=======================================")
            print("--- Terima Kasih Telah Menggunakan Program ---")
            print("=======================================\n")
            return False
        else:
            print("Input tidak valid. Masukkan 'y' atau 'n'.")

def main():
    """Fungsi utama untuk menjalankan program data siswa."""
    while True:
        display_menu()
        pilihan = get_menu_choice()

        if pilihan == 1:
            input_student_data()
        elif pilihan == 2:
            display_student_count()
        elif pilihan == 3:
            search_student_data()
        elif pilihan == 4:
            sort_student_data()
        elif pilihan == 5:
            print_all_students()
        elif pilihan == 6:
            print("\n=====================================")
            print("===== Terima Kasih, Sampai Jumpa =====")
            print("=====================================\n")
            break # Keluar dari loop utama, sehingga mengakhiri program
        
        # Bagian ini hanya tercapai jika pilihan bukan 6
        if not ask_to_continue():
            break # Keluar dari loop utama jika pengguna memilih 'n'

if __name__ == "__main__":
    main()


# Kode Asli yang Dihapus/Dimodifikasi:
# ulang = "Y"
# while ulang.upper() == "Y":
    # ... (logika menu lama) ...
    # if pilihan == 1:
        # ...
        # ulang = input("Apakah anda ingin kembali ke Menu? [y/n] : ").upper()
        # if ulang == "N":
            # print("\n=======================================")
            # print("---Terima Kasih Telah Menginput Data---")
            # print("=======================================\n")
    # elif pilihan == 4:
        # print("---Pilihan Pengurutan Data---")
        # print("1. Berdasarkan Nama")
        # print("2. Berdasarkan Kelas")
        # ...
        # (Original sorting logic had potential issue if 'kelas' was not int)
        # data_siswa.sort(key=lambda m: int(m["kelas"])) 
        # print("Data Siswa berhasil diurutkan berdasarkan Semester terkecil")

    # ... (blok elif lainnya dengan logika ulang yang berulang) ...

    # else:
    #     print("Pilihan anda tidak valid. Silakan pilih menu [1-5]")
    #     ulang = "Y" # This forced loop continuation for invalid main menu choice
