# Common Form
ulang = 10
for i in range(ulang):
    print("Perulangan Ke-" + str(i))

# Variable i Berfungsi Untuk Menampung Index
# range() berfungsi Untuk Membuat List Dengan Range dari 0-10
# str() Berfungsi Mengubah Data Integer Ke String

# Use List
print(' ')
i = ['Kak Sarah','Dek Adel','Nadine', 'Taqia','Kak Tasya','Kurumi(My Waifu)']
for nama in i:
    print("- Nama : ",nama)

    
# Use Index
print(' ')
item = ['Python','Java','JavaScript','Golang','C++','PHP']
for index in range(len(item)):
    print("Programming : ",item[index])
