# Menulis File
with open('data.txt', 'w') as f:
    f.write("Contoh Teks")
    
# Membaca File
with open('data.txt', r) as f:
    konten = f.read()