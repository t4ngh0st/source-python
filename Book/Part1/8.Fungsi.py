print('\n')
def ucapan(input_nama):
    print("Selamat Datang " + input_nama)
    print("Semoga Anda Beruntung Selalu")
ucapan("Bocah Tengik")

# Custom Fungsi Dengan Parameter Sendiri
print('\n')
input_nama1 = input("Masukkan Namanya ? ")
def ucapan1(input_nama1):
    print("Selamat Datang " + input_nama1)
    print("Semoga Anda Beruntung Selalu")
ucapan1(input_nama1)

# Parameter Tidak Terbatas
def panggil(*nama):
    print("\nDaftar Buah Yang Dibeli")
    for buah in nama:
        print("- " + buah)
# Pemanggilan Fungsi
panggil("Apel", "Anggur", "Langsat", "Rambutan")

# Parameter Tidak Terbatas(Custom)
list1 = input("\n[?] Masukkan Buah Yang Ingin Dibeli ? ")
def panggil(*nama):
    print("[+] Daftar Buah Yang Dibeli")
    for buah in nama:
        print("- " + buah)
# Pemanggilan Fungsi
panggil(list1, "Anggur", "Langsat", "Rambutan")

# Argumen Default
def nama(pesan, ucapan="Selamat"):
    print(ucapan, pesan)
nama("Rita")
nama("Anto, Apa Kabar")