# Membuat List Kosong
barang = []
print(barang)
print(" ")

# Membuat List Dengan Isi 1 Item
barang1 = ['Coklat']
print(barang1)
print(" ")

# Membuat List Dengan Banyak Item
barang2 = ['Android', 'IOS', 'Linux', 'MacOS', 'Windows']
print(barang2)
print(barang2[0]) # android
print(barang2[1]) # IOS
print(barang2[2]) # Linux
print(barang2[3]) # MacOS
print(barang2[4]) # Windows
print(" ")

# Membuat List Dengan Tipe Random
laci = ['Buku', 21, True, 3.14]
print(laci)
print(" ")

# Random
my_brother = ['Bang Ashidiqqi Osama', 'Bang Luthfi Abrar', 'Bang Alferrodin', 'Om Aril']
print("Isi My Brother Index Ke-2 Adalah : ",my_brother[2])
# Menampilkan Semua Daftar my_brother
print("Semua Teman: Ada {} orang".format(len(my_brother)))
for Brother in my_brother:
    print(Brother)
    print(" ")
    
# Fungsi len() Berguna Mengambil Panjang List

# Mengganti Nilai List
buah_awal = ['Apel', 'Jeruk', 'Mangga', 'Durian']
print(buah_awal)
buah_awal[2] = 'Anggur'
print(buah_awal)
print(" ")

# Mengganti Nilai List(Custom)
buah_awal = ['Apel', 'Jeruk', 'Mangga', 'Durian']
print(buah_awal)
buah_awal[2] = input("Masukkan Buah Baru[2] : ")
print(buah_awal)
print(" ")

# Mengganti Nilai List(Custom)1
buah_awal = ['Apel', 'Jeruk', 'Mangga', 'Durian']
print(buah_awal)
print("Index : 0,1,2,3")
user = int(input("Masukkan Index Yang Ingin Diubah : "))
buah_awal[user] = input(f"Masukkan Buah Baru[{user}] : ")
print(buah_awal)
print(" ")

# Menambah Item List
# prepend(item) Menambah Item Dari Depan
# append(item) Menambah Item Dari Belakang
# insert(index, item) Menambah Item Dari Index Tertentu
# Prepend Ex:
buah_awal = ['Apel', 'Jeruk', 'Mangga', 'Durian']
append.buah_awal("Semangka")
print(buah_awal)
print(" ")
# Append Ex:
buah_awal = ['Apel', 'Jeruk', 'Mangga', 'Durian']
buah_awal.append("Semangka")
print(buah_awal)
print(" ")
# Insert Ex:
nomor = [1, 2, 3, 5, 6, 7]
nomor.insert(3, 4)
print(nomor'Empat')
print(" ")

# Note : Index Dimulai Dari '0'