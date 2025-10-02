import os, socket, subprocess, time, threading, urllib, wmi
from datetime import datetime
from queue import Queue
from bs4 import BeautifulSoup

def getIP():
    host = input("URL >> ")
    print(socket.gethostbyname(host))

def ping_sweep():
    net = input("IP Address Target : ")
    net1 = net.split('.')
    a = '.'
    net2 = net1[0]+a+net1[1]+a+ne1[2]
    st1 = int(input("Nomor Awal  : "))
    en1 = int(input("Nomor Akhir : "))
    en1 = en1+st1
    t1 = datetime.now()
    print("Ping Sweep Dalam Proses")
    for ip in range(st1,en1):
        alamat = net2+str(ip)
        res = subprocess.call(['ping', alamat])
        if res == 0:
            print("Ping Ke", alamat, "OK")
    t2 = datetime.now()
    total = t2 - t1
    print("Selesai Selama: ",total)
    
def tracroute():
    ip = input("IP Address Target : ")
    result = os.popen("Pathping "+str(ip))
    for i in results:
        print(i)
        
def tcp_sweep():
    net = input("IP Address Target : ")
    net1 = net.split('.')
    a = '.'
    net2 = net1[0]+a+net1[1]+a+net1[2]+a
    st1 = int(input("Nomor IP Awal  : "))
    en1 = int(input("Nomor IP Akhir : "))
    port = int(input("Nomor Port : "))
    en1 = en1+1
    tl = datetime.now()
    
    def scan(addr):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((addr,port))
        if result == 0:
            return 1
        else:
            return 0
        
    def run1():
        for ip in range(st1,en1):
            addr = net+str(ip)
            if (scan(addr)):
                print(addr, "ON")
    run1()
    t2 = datetime.now()
    total = t2-t1
    print("Scanning Finish IN :", total)
    
def port_scanner():
    socket.setdefaulttimeout(0.25)
    print_lock = threading.Lock()
    target = input("IP Target : ")
    t_IP = socket.gethostbyname(target)
    print("Memulai Scanning Target : ",t_IP)
    
    def port_scanner(port):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            con = s.connect((t_IP, port))
            with print_lock:
                print(port, ' OPEN')
                con.close()
        except:
            pass
    def threader():
        while True:
            worker = q.get()
            portscan(worker)
            q.task_done()
            
    q = Queue()
    StartTime = time.time()
    
    for x in range(100):
        t = threading.Thread(target=threader)
        t.daemon = True700
        t.start()
    for worker in range(1, 700):
        q.put(worker)
        
    q.join()
    print("Waktu Yang Digunakan : ", time.time() - StartTime)