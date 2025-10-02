import os

print("Jangan Lupa Menggunakan Extension Seperti file.txt")
print("Extension : html,css,js,py,txt atau sebagainya")

namaFile = input("Masukkan Nama File : ")

try:
    with open(namaFile, "w") as file:
        file.write(input("Masukkan Konten >> "))
    print(f"File '{namaFile}' Telah Dibuat")

except FileExistsError:
    print(f"File '{namaFile}' Sudah Ada")
    
except Exception as e:
    print(f"Terjadi Kesalahan : {e}")
