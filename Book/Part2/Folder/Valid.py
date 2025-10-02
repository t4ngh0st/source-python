# Mengetahui Ada Tidaknya Suatu Folder 
import os

if os.path.isdir("Folder Test")==True:
    print("Ada")
else:
    print("Tidak Ada")