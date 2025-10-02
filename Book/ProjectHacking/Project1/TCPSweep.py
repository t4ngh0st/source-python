import socket
from datetime import datetime

net = input("IP Address >> ")
net1 = net.split('.')
a = '.'
net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Nomor IP Awal  : "))
en1 = int(input("Nomor IP Akhir : "))
port = int(input("Nomor Port    : "))
en1 = en1 + 1
t1 = datetime.now()
def scan(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((addr,port))
    if result == 0:
        return 1
    else:
        return 0
    
def run():
    for ip in range(st1,en1):
        addr = net2 + str(ip)
        if (scan(addr)):
            print(addr, "ON")
            
run()
t2 = datetime.now()
total = t2 - t1
print("Scanning Finish ON : ",total)