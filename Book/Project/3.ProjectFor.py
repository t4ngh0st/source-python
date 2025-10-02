# Variabel untuk menyimpan angka
angka = int(input("Masukkan angka yang ingin dikalikan: "))

print("Tabel perkalian", angka, ":")
# Loop for untuk melakukan iterasi dari 1 sampai 5
for i in range(1, 6):
  # Operator perkalian (*)
  hasil_kali = angka * i
  # Operator penugasan dan mencetak hasil
  print(angka, "x", i, "=", hasil_kali)

  
angka1 = int(input("Masukkan angka yang ingin ditambahkan: "))
print("Tabel penambahan", angka1, ":")
  
for i in range(1, 10):
    hasil_penambahan = angka1 + i
    print(angka1, "+", i, "=", hasil_penambahan)