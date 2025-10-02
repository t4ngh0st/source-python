# List Multidimensi adalah List yang Memiliki List dalam List
# List Multimedia biasanya digunakan untuk menyimpan struktur data yang kompleks seperti:
# Tabel,Matriks,Graph,Tree dan sebagainya

# List Multidimensi dengan 2 Dimensi
list_minuman = [
    ['Kopi', 'Susu', 'Teh'],                    # List Multidimensi Index 0
    ['Jus Apel', 'Jus Melon', 'Jus Jeruk'],     # List Multidimensi Index 1
    ['Es Kopi', 'Es Campur', 'Es Teler']        # List Multidimensi Index 2
]

# Cara Mengakses List Multidimensi
print(list_minuman[0][0]) # Misalkan Ingin Mengambil Kopi
print(list_minuman[1][0]) # Misalkan Ingin Mengambil Jus Apel
print(list_minuman[2][0]) # Misalkan Ingin Mengambil Es Kopi
print(" ")

# Menampilkan List Multidimensi
for menu in list_minuman:
    for minuman in menu:
        print(minuman)
print(" ")
        
# Mengetahui Nilai Panjang,Minimum,Maksimum dan Jumlah
list1 = [2, 3, 4, 1, 32]
print(len(list1)) # Output 5
print(max(list1)) # Output 32
print(min(list1)) # Output 1
print(sum(list1)) # Output 42

# Note:
# Fungsi sum() : Menjumlahkan Semua Elemen Yang Ada dalam List
# Fungsi len() : Menghitung Jumlah yang ada di dalam List