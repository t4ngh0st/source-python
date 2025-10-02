def user():
    nama = input("Masukkan Nama Anda >> ")
    try:
        umur = int(input("Masukkan Umur Anda >> "))
    except ValueError:
        print("Umur Harus Berupa Angka")
        return None, None, None # Kembalikan None jika input tidak valid
    alamat = input("Masukkan Alamat Anda >> ")
    return nama, umur, alamat # Kembalikan nilai yang diinput

def Dic(nama, umur, alamat):
    user_data = {
        "Nama": nama,
        "Umur": umur,
        "Alamat": alamat
    }
    return user_data # Kembalikan dictionary yang sudah dibuat

def tabel():
    print("\n===== Menu =====")
    print("[1] Create Dictionary")
    print("[2] Exit")
    print("================\n")
    
    try:
        pilihan = int(input("[?] Masukkan Opsi >> "))
    except ValueError:
        print("Opsi Harus Berupa Angka")
        return # Keluar dari fungsi jika input tidak valid
    
    if pilihan == 2:
        print("Bye Bye...")
        exit()
    elif pilihan == 1:        
        nama_input, umur_input, alamat_input = user() 
        if nama_input is not None: # Pastikan input dari user() valid
            data = Dic(nama_input , umur_input, alamat_input) # Panggil Dic dengan hasil input
            print("\nDictionary Berhasil Dibuat:")
            for key, value in data.items():
                print(f"{key}: {value}")
    else:
        print("Opsi Tidak Valid")
        
# Menjalankan program utama jika skrip ini dieksekusi langsung
if __name__ == "__main__":
    tabel()