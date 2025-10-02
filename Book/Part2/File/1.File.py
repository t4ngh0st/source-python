import os

f = open('HasilFile.py','w+')
f.write('print("Hello World")\n')
f.write('user=input("Masukkan Nama Anda :")\n')
f.write('print(f"Halo! {user}")')
f.close
print('File Tersebut Berada Di', os.getcwd())