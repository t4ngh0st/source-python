def segiempat():
    print("\nMenghitung Luas SegiEmpat")
    panjang = int(input("Panjang = "))
    lebar = int(input("Lebar = "))
    print("Luas = " + str(panjang * lebar))

def segitiga():
    print("\nMenghitung Luas Segitiga")
    alas = int(input("Alas = "))
    tinggi = int(input("Tinggi = "))
    print("Luas = " + str(alas*tinggi/2))

def layang2():
    print("\nMenghitung Luas Layang-Layang")
    diagonal1 = int(input("Diagonal 1 = "))
    diagonal2 = int(input("Diagonal 2 = "))
    print("Luas = " + str(diagonal1*diagonal2/2))

def trapesium():
    print("\nMenghitung Luas Trapesium")
    atap = int(input("Atap = "))
    alas = int(input("Alas = "))
    tinggi = int(input("Tinggi = "))
    print("Luas = " + str((alas+atap)*tinggi/2))
    
def show_menu():
    print("\n===== Menu =====")
    print("[1] SegiEmpat")
    print("[2] Segitiga")
    print("[3] Layang-Layang")
    print("[4] Trapesium")
    print("[5] Exit")
    
    user = int(input("[?] Masukkan Opsi >> "))
    
    if user == 5:
        print("Bye Bye...")
        exit()
    elif user == 1:
        segiempat()
    elif user == 2:
        segitiga()
    elif user == 3:
        layang2()
    elif user == 4:
        trapesium()
    else:
        print("Error")

# Menjalankan program utama jika skrip ini dieksekusi langsung
if __name__ == "__main__":
    show_menu()