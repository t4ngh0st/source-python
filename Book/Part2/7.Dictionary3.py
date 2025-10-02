# Menambah Item Dictionary
# Menggunakan method update() untuk menambah isi ke directionary
# Membuat Dictionary User,Method Ini Juga Berfungsi Untuk Mengubah Nilai

user = {
    'nama': 'Udin'
}

# Menambah key password dan valuenya
print("====== Method Add Item Directory ======")
user.update({'password': 'admin#123'})
print(user)

# Mengubah key nama
print("====== Method Change Value in Key ======")
user.update({'nama': 'PDN'})
print(user)


# MengCopy Directory
print(" ")
print('='*50)
x = {'username': 'Admin', 'pw': ['123', 'qwerty', '12345']}
y = x.copy()
y['username'] = 'PDN'
y['pw'].remove('123')

print(x)
print(y)
print(" ")


# Mengambil Panjang Dictionary
# Untuk Mengambil Jumlah Data atau Panjang Dictionary,Kita Bisa Menggunakan Fungsi
# len().Ex:
# Membuat Dictionary
book = {
    'Python': 'Bahasa Pemograman Yang Cocok Untuk Pemula',
    'Bash': 'Bahasa Pemograman Yang Terintegrasi Di Linux & MacOS',
    'Powershel': 'Bahasa Pemograman Yang Dikembangkan Oleh Microsoft'
}
for key, value in book.items():
    print(f"[-] {key}: {value}")
print("="*70)
print("Total Buku: %d" % len(book))