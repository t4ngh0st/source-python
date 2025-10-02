# MD5 Cracking Dengan Metode Dictionary Attack

import hashlib
import time

counter = 1

md5_hash = input("Hash MD5 : ")
pwdFile = input("Alamat WordList : ")

try:
    pwd = open(pwdFile,"r")
except:
    print("\nFile Tidak Ditemukan")
    quit()

for password in pwd:
    md5 = haslib.md5()
    md5.update(password.strip().encode('ascii'))
    start = time.time()
    print = ("Cona Password %d: %s" % (counter,password.strip()))
    
    counter += 1
    end = time.time()
    tTime = end - start
    
    if md5_hash.strip() == md5.hexdigest():
        print("\nPassword Ditemukan.\nPasswordnya Adalah : %s" % password.strip())
        print("Total Waktu : ", tTime, "Second")
        time.sleep(10)
        break
    else:
        print("\nPassword Tidak Ditemukan")