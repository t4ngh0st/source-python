from stegano import lsb

gambar1 = input("Gambar Awal : ")
gambar2 = input("Gambar Yang Akan Berisi Pesan : ")
pesan = input("Pesan Rahasia : ")

# Sembunyikan Pesan
secret = lsb.hide(gambar1, pesan)

# Create File Gambar Baru
secret.save(gambar2)

# Ekstrak Pesan
print(lsb.reveal(gambar2))