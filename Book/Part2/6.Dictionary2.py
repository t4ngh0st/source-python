# Mengubah Nilai Item Dictionary
# Membuat Dictionary
print(">> Membuat Dictionary")
skill = {
    'utama': 'Python',
    'lainnya': ['Bash','Powershell','JS']
}

# Mencetak Isi Skill Utama
print(skill['utama'])
print('Skill Utama', skill['utama'])

# Mengubah Isi Skill Utama
skill['utama'] = 'C'
# Mencetak Ulang Isi Skill Utama
print(skill['utama'])
print('Skill Utama', skill['utama'])
print(" ")



# Menghapus Item Dari Dictionary
# Untuk Menghapus Nilai Dictionary Menggunakan Perintah del dan method pop()
# method pop() adalah method yang berfungsi untuk mengeluarkan item dari directory
# del adalah fungsi untuk menghapus suatu Variable dari Memori

# Ex:
# del function
# Membuat Dictionary
print(">> del function")
skill1 = {
    'utama': 'Python',
    'lainnya': ['Bash','Powershell','JS']
}
# Mencetak Isi Skill Utama
print(skill1)

# Menghapus Skill Utama
del skill1['utama'] 
# Cetak Kembali
print(skill1)
print(" ")


# method pop()
print(">> method pop()")
skill2 = {
    'utama': 'Python',
    'lainnya': ['Bash','Powershell','JS']
}
# Mencetak Isi Skill Utama
print(skill2)

# Menghapus Skill Utama
skill2.pop('utama') 
# Cetak Kembali
print(skill2)

# Menggunakan clear()
# Menghapus Semua Dic Skill
skill2.clear() 
# Cetak Kembali
print(skill2)
