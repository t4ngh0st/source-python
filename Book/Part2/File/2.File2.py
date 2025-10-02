# Membaca Isi File
f = open('File Test', 'r')
for i in range(2):
    print(str(i) + ': ' + f.readline())
# Output:
# 0:
# 1:

f = open('File Test', 'r')
a = 'Hello World'
for char in f.read():
    a = a+char
print(a)
# Output:
# Hello World


# >> Menghapus File

# import os
# os.remove('Nama File')

# Menghapus Folder
# import os
# os.rmdir('Nama Folder')

# Mengganti Nama File
# import os
# os.rename('Nama File Lama', 'Nama File Baru')

# Mengetahui Ada Tidaknya Suatu File
# import os
# if os.path.isfile("Nama File")==True:
#     print("Ada")
# else:
#     print("Tidak Ada")