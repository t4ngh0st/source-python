import random

def Game():
    print("""
    ============================
    |  Selamat Datang Di Game  |
    |       Tebak Angka        |
    ============================
    """)
    
    angka = random.randint(1, 10)
    percobaan = 0
    skor = 100
    
    while True:
        percobaan += 1
        print("|_^_| |_^_| " *  5)
        tebakan = input("\nMasukkan Tebakan Anda(1-10) : ")
        
        # Validasi Input
        if not tebakan.isdigit():
            print("Masukkan Angka Yang Valid!")
            continue
        
        tebakan = int(tebakan)
        
        if tebakan < 1 or tebakan > 10:
            print("Angka Harus Antara 1 & 10")
            continue
        
        # Periksa Tebakan
        if tebakan == angka:
            print(f"\nSelamat! Anda Menebak Dengan Benar Dalam {percobaan} Percobaan")
            print(f"Skor Anda : {skor}")
            break
        elif tebakan < angka:
            print("Terlalu Kecil! Coba Lagi")
            skor -= 10
        else:
            print("Terlalu Besar! Coba Lagi")
            skor -= 10
        
        # Beri Petunjuk
        if percobaan == 5:
            if angka %2 == 0:
                print("Petunjuk: Angka Random Adalah Bilangan Genap")
            else:
                print("Petunjuk: Angka Random Adalah Bilangan Ganjil")
        elif percobaan == 8:
            print(f"Petunjuk: Angka Random Antara {max(1, angka-10)} dan {min(10, angka+10)}")
        
        if skor <= 0:
            print("\nSkor Anda Sudah 0. Game Over")
            print(f"Angka Random Adalah : {angka}")
            break

def jan_ken_pon():
    print("""
    =============================
    |       Jan Ken Pon         |
    |           Game            |
    =============================
    """)
    
    pilihan = ['batu', 'gunting', 'kertas']
    skor_pemain = 0
    skor_komputer = 0
    
    while True:
        print(f"\nSkor - Anda: {skor_pemain} | Komputer: {skor_komputer}")
        pilihan_pemain = input("Pilih (batu/gunting/kertas) atau 'keluar' untuk berhenti: ").lower()
        
        if pilihan_pemain == 'keluar':
            print("\nPermainan selesai!")
            print(f"Skor Akhir - Anda: {skor_pemain} | Komputer: {skor_komputer}")
            break
            
        if pilihan_pemain not in pilihan:
            print("Pilihan tidak valid!")
            continue
            
        pilihan_komputer = random.choice(pilihan)
        print(f"Anda memilih: {pilihan_pemain}")
        print(f"Komputer memilih: {pilihan_komputer}")
        
        # Tentukan pemenang
        if pilihan_pemain == pilihan_komputer:
            print("Hasil: Seri!")
        elif (pilihan_pemain == 'batu' and pilihan_komputer == 'gunting') or \
             (pilihan_pemain == 'gunting' and pilihan_komputer == 'kertas') or \
             (pilihan_pemain == 'kertas' and pilihan_komputer == 'batu'):
            print("Hasil: Anda menang!")
            skor_pemain += 1
        else:
            print("Hasil: Komputer menang!")
            skor_komputer += 1

def main():
    while True:
        print("\n====== Menu Game ======")
        print("1. Game Tebak Angka")
        print("2. Game Jan Ken Pon")
        print("3. Keluar")
        
        user = int(input("Pilih Opsi(1-3) : "))
        
        if user == 1:
            Game()
        elif user == 2:
            print("Coming Soon")
            break
        elif user == 3:
            print("Bye Bye Bye")
            break
        else:
            print("Pilihan Tidak Valid")

if __name__ == "__main__":
    main()