# Modul Ini Berguna Memanggil Program Lain,Termasuk Program Untuk Jaringan Seperti:Ping

import subprocess

for ping in range(1,10):
    alamat = "127.0.0." + str(ping)
    res = subprocess.call(['ping', 'alamat'])
    if res == 0:
        print("Ping To", alamat, "Success")
    elif res == 2:
        print("Ping To", alamat, "Not Response")")
    else:
        print("Ping To", alamat, "Failed")