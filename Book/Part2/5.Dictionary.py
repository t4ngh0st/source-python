# Dictionary adalah Data yang berbentuk Seperti kamus
# Untuk Mendeklasi sebuah Dictionary,Python Menggunakan {}
# Ex:
info = {
    "Nama" : "Muhammad Luthfi Fakhmar"
    "Sekolah" : "SMKN 5 Takengon",
    "Kelas" : "XI",
    "Jurusan" : "Rekayasa Perangkat Lunak"
}

# Hal Yang Wajib Ada Di Dalam Dictionary
# - Nama Dictionary
# - Key
# - Value
# - Tanda Kurung Kurawal "{}"

# Antara Key dan Value Dipisah dengan titik dua (:) dan apabila
# terdapat lebih dari satu item,maka dipisah dengan tanda koma(,)

# Ex 1 Item
nama_dict = {
    "key" : "value",
}

# Ex 3 Item
nama_dict = {
    "key" : "value",
    "key" : "value",
    "key" : "value",
}


# Isi dari Dictionary Dapat Berupa:
# String
# Integer
# Objek
# List
# Tuple
# Dictionary
# Boolean
# dan sebagainya

# Ex:
info_Lain = {
    "Nama": "Lainnya",
    "Umur": 16,
    "Kelas": "X",
    "Jurusan": "Teknik Komputer dan Jaringan",
    "Hobi" : ['Badminton', 'Healing', 'Movies'],
    "Siswa": True,
    "etc":  {
        "EmailBackup": "lain123456@gmail.com",
        "EmailUtama": "lain123456@gmail.com",
        "No": "082162936017"
    }
}

print("Namanya : %s" % info_Lain["Nama"])
print("Umurnya : %s" % info_Lain["Umur"])
print("Kelasnya : %s" % info_Lain["Kelas"])
print("Jurusannya : %s" % info_Lain["Jurusan"])
print("Hobi : %s" % info_Lain["Hobi"])
print("Siswanya : %s" % info_Lain["Siswa"])
print("Email : %s" % info_Lain["etc"]["EmailUtama"])
print("No : %s" % info_Lain["etc"]["No"])
print("-"*30)

# Menggunakan method get() untuk mengambil nilai Dictionary
# Ex:
print("Namanya : %s" % info_Lain.get("Nama"))
print("Umurnya : %s" % info_Lain.get("Umur"))
print("Kelasnya : %s" % info_Lain.get("Kelas"))
print("Jurusannya : %s" % info_Lain.get("Jurusan"))
print("Hobi : %s" % info_Lain.get("Hobi"))
print("Siswanya : %s" % info_Lain.get("Siswa"))
print("Email Utama : %s" % info_Lain.get("etc").get("EmailUtama"))
print("Email Backup : %s" % info_Lain.get("etc").get("EmailBackup"))
print("No : %s" % info_Lain.get("etc").get("No"))
print("-"*30)


# isi dari Dictionary
# Nama Berisi String Yunita Uswandari
# Umur Berisi Integer 16
# Kelas Berisi String X
# Jurusan Berisi String Teknik Komputer dan Jaringan
# Hobi Berisi List ['Badminton', 'Healing', 'Movies']
# Siswa Berisi Boolean True
# etc Berisi Dictionary

# Membuat Dictionary Menggunakan Constructor dict() denga parameter key dan value
# Ex:
warna_buah = dict(
    apel = "merah",
    jeruk = "Oranye",
    mangga =  "hijau"
)

print("-"*30)
print(f"Warna Apel : {warna_buah['jeruk']}")
