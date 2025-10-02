# Membuat Time Bomb
import time

jawab = 'y'

while jawab == 'y':
    waktu = time.starttime("%d/%m/%Y, %H", time.localtime())
    if str(waktu) == '08/06/2019, 11':
        print("Waktu Action")
    else:
        print("Belum Waktu")
        if str(waktu) == '08/06/2019, 11:
        break
exit()

# 1 Jam(Kode %H Adalah hour),Bentuk Format Waktu Seperti Ini:
# '08/06/2019, 11:17:50' adalah "%d/%m/%Y, %H:%M:%S"