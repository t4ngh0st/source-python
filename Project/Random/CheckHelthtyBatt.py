# ==================================================================
# Script Lama

# print("====================")
# nilai_a = input("Energy Full >> ")
# nilai_b = input("Energy Full Design >> ")
# print("====================")
# nilai_c = float(nilai_a / nilai_b)
# print("====================")
# print(c)

# kali = 100
# hasil = nilai_c * kali
# print(hasil)

# ==================================================================


import sys # Tambahkan ini untuk bisa menggunakan sys.exit()

print("====================")
# Mengambil input dari pengguna. Sebaiknya nama variabel input string dibedakan.
# Juga, saya tambahkan keterangan pada prompt input agar lebih jelas.
nilai_a_str = input("Energy Full (kapasitas saat ini) >> ")
nilai_b_str = input("Energy Full Design (kapasitas desain) >> ")
print("====================")

try:
    # Konversi input string menjadi angka (float) agar bisa dihitung.
    # Di skrip lama, operasi nilai_a / nilai_b dilakukan pada string, yang menyebabkan error.
    nilai_a = float(nilai_a_str)
    nilai_b = float(nilai_b_str)
except ValueError:
    # Jika pengguna memasukkan teks yang bukan angka, beri pesan error dan keluar.
    print("Error: Input harus berupa angka (misalnya 40.5 atau 50).")
    sys.exit(1) # Keluar dari program

# Mencegah error pembagian dengan nol jika Energy Full Design adalah 0.
if nilai_b == 0:
    print("Error: 'Energy Full Design' tidak boleh nol.")
    sys.exit(1) # Keluar dari program

# Hitung rasio kesehatan baterai. Ini adalah 'nilai_c' yang dimaksud di skrip lama.
nilai_c = nilai_a / nilai_b

# Di skrip lama, ada 'print(c)' yang salah ketik (seharusnya nilai_c) dan
# akan mencetak rasio mentah (misal 0.81).
# Jika ingin melihat rasio, bisa tambahkan baris seperti:
# print(f"Rasio (nilai_c): {nilai_c:.2f}") # :.2f untuk 2 angka di belakang koma

# 'kali' untuk persentase. Di skrip lama, '100%' adalah syntax error.
kali = 100

# Hitung hasil akhir dalam bentuk persentase.
hasil = nilai_c * kali

# Tampilkan hasil dengan format yang lebih jelas dan sesuai contoh.
# Menggunakan f-string untuk memformat output.
# :.0f digunakan untuk membulatkan hasil ke bilangan bulat terdekat (misal 81% bukan 81.0%).
print(f"Kesehatan Baterai: {hasil:.0f}%")
# Menampilkan detail perhitungan seperti contoh yang Anda berikan:
print(f"Perhitungan: ({nilai_a} / {nilai_b}) * {kali}% = {hasil:.0f}%")

