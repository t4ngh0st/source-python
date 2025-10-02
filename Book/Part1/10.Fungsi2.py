def menu():
    print("\n===== Menu Tabel =====")
    print("[1] Luas")
    print("[2] Panjang")
    print("[3] Lebar")
    print("[4] Exit")
    print("======================\n")
    
    user = int(input("[?] Masukkan Opsi >> \n"))
    
    if user == 4:
        print("Bye Bye...")
        exit()
    elif user == 1:
        luas()
    elif user == 2:
        panjang()
    elif user == 3:
        lebar()
    else:
        print("Error")
    
def luas(panjang, lebar):
    return (panjang * lebar)

panjang = int(input("Masukkan Nilai Panjang : "))
lebar = int(input("Masukkan Nilai Lebar : "))
print("Luas = " + str(luas(panjang, lebar)))

def panjang(luas, lebar):
    return(luas / lebar)
luas = int(input("Masukkan Nilai Luas : "))
lebar = int(input("Masukkan Nilai Lebar : "))
print("Panjang = " + str(panjang(luas, lebar)))

def lebar(luas, panjang):
    return(luas / panjang)
luas = int(input("Masukkan Nilai Luas : "))
panjang = int(input("Masukkan Nilai Panjang : "))
print("Lebar = " + str(lebar(luas, panjang)))

# Menjalankan program utama jika skrip ini dieksekusi langsung
if __name__ == "__main__":
    menu()