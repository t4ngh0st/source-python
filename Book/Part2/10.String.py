# String Dapat Ditulis Dengan Tiga Cara :
# Diapit Tanda Petik Tunggal (');
# Diapit Tanda Petik Ganda (");
# Diapit Tiga Tanda Petik Tunggal Atau Tiga Tanda Petik Ganda

print('Dibatasi Tanda Petik Tunggal')
print("Dibatasi Tanda Petik Ganda")
print()
print('"Petik Ganda Dalam Petik Tunggal" Diluar Tanda Petik Ganda')
print("'Petik Tunggal Dalam Petik Ganda' Diluar Tanda Petik Tunggal")
print()
print('\'Petik Tunggal\' Dalam Petik Tunggal Harus Menggunakan Karakter +escape')
print("\"Petik Ganda\" Dalam Petik Ganda")

# Fungsi Yang Digunakan Untuk Mengelola String
# 
# ====================================================================================
#   Fungsi          Kegunaan           Contoh Perintah             Hasil
#                                      a="Selamat siang"
# ====================================================================================
#   [:]        Mengambil Sebagian       print(a[0:2])              Se
# ====================================================================================
#               Karakter String
#   len        Mengetahui Panjang       print(len(a))              13
#               Karakter String
# ====================================================================================
#              Menghilangkan White
#   strip()     Space sebelum Dan       print(a.strip())        Selamat
#             Sesudah Karakter String                           siang
# ====================================================================================
#              Menghasilkan Kalimat
#   lower()     Berhuruf Kecil Semua    print(a.lower())        selamat siang 
#              (lower case)
# ====================================================================================
#              Menghasilkan Kalimat
#   upper()    Berhuruf Kapital Semua   print(a.upper())        SELAMAT SIANG
#              (upper case)
# ====================================================================================
#   title()    Setiap Huruf Awal Kata
#                Menjadi Kapital        print(a.title())        Selamat Siang
# ====================================================================================
#              Mengganti Karakter/Kata
#  replace()   Dalam String Dengan      print(a.replace         Selamat malam
#              Karakter/Kata Yang Lain  ("siang","malam"))
#=====================================================================================
#   find()     Mencari Posisi Suatu     print(a.find("ia"))     9 = s iang
#               Karakter                
# ====================================================================================
#              Memotong String Dengan
#   Split()   Suatu Pemisah Untk Di     print(a.split(" "))     ['Selamat', 'siang']
#              Jadikan List
# ====================================================================================
#              Mengetahui Apakah Semua
# isnumeric()  Karakter String Adalah   print(a.isnumeric())        FALSE
#              Angka
# =====================================================================================



# Karakter Backlash Yang Digunakan Untuk Memanipulasi String
# 
# ==========================================================
#       Notasi Backlash             Keterangan
#           \a                  Bell Atau Peringatan
#           \b                  Backspace
#           \e                  Escape
#           \f                  Formfeed
#           \n                  Baris Baru
#           \r                  Carrige Return
#           \s                  Space
#           \t                  Tab
#           \v                  Tab Vertikal
# =============================================================