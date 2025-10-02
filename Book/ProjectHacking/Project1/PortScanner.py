import socket
import time
import threading
from queue import Queue

socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()
target = input('IP Target : ')
t_IP = socket.gethostbyname(target)
print("Memulai Scan Target: ",t_IP)

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((t_IP,port))
        with print_lock:
            print(port,"Open")
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

startTime = time.time()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,1000):
    q.put(worker)

q.join()
print("Waktu Yang Digunakan : ",time.time() - startTime," Detik")