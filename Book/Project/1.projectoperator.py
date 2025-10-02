print("=" * 25)
print("[1] Penambahan   (+)",'\n'
      "[2] Pengurangan  (-)",'\n'
      "[3] Perkalian    (x)",'\n'
      "[4] Pembagian    (/)",'\n'
      "[5] Keluar",'\n')
print("=" * 25,'\n')
user = int(input("Masukkan Pilihan Mu >> "))

if user == 5:
    print("Sampai Jumpa :(")
    exit()
elif user == 1:
    a = int(input("Masukkan Nilai Pertama >> "))
    b = int(input("Masukkan Nilai Kedua   >> "))
    print(a + b)
elif user == 2:
    a = int(input("Masukkan Nilai Pertama >> "))
    b = int(input("Masukkan Nilai Kedua   >> "))
    print(a - b)
elif user == 3:
    a = int(input("Masukkan Nilai Pertama >> "))
    b = int(input("Masukkan Nilai Kedua   >> "))
    print(a * b)
elif user == 4:
    a = int(input("Masukkan Nilai Pertama >> "))
    b = int(input("Masukkan Nilai Kedua   >> "))
    if b == 0:
      print("Error........")
    else:
        print(a / b)
else:
    print("Error........")