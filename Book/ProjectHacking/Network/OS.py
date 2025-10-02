# Modul os.popen Berguna Memanggil Program Lain

import os

ip = input("IP Address Target > ")
result = os.popen("pathping" + str(ip))
for i in result:
    print(i)
    
# Akan Menampilkan Hasil Traceroute Ke IP Address Target Yang Kita Inginkan
# Traceroute Adalah jalur Perjalanan Paket ICMP Yang Kita Kirim Ke Komputer Target