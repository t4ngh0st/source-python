import subprocess
from datetime import datetime

net = input("IP Address Target : ")
net1 = net.split('.')
a = '.'
net2 = net1[0] + a + net[1] + a + net1[2] + a
st1 = int(input("Nomor Awal : "))
en1 = int(input("Nomor Akhir : "))
en1 = en1 + 1
t1 = datetime.now()
print("Ping Sweep Dalam Proses...")
for ip in range(st1,en1):
    alamat = net2 + str(ip)
    res = subprocess.call(['ping', alamat])
    if res == 0:
        print("Ping Ke ", alamat," OK")
t2 = datetime.now()
total = t2-t1
print("Selesai Selama : ",total)