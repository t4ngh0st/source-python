jumlah_elemen = 5
angka = [] # Mebuat List Angka
sum = 0

for i in range(jumlah_elemen):
    value = eval(input("[?] Masukkan Angka = "))
    angka.append(value)
    sum += value
rata_rata = sum / jumlah_elemen
hitung = 0 # Banyak Angka Di Atas Rata-Rata
for i in range(jumlah_elemen):
    if angka[i] > rata_rata:
        hitung += 1
        print("Rata-ratanya adalah: ",rata_rata)
        print('Banyaknya  Angka Diatas rata-rata: ', hitung)
        
# Fungsi eval() : Mengubah String menjadi Integer atau Float