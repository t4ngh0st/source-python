# Belum Sempurna
import socket

def scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        service = sock.recv(1024)
        service = service.decode('utf-8')
        service = service.split('\n')
        print(f"Port {str(port)} IS Open", end="  ")
        print(service)
    except ConnectionRefusedError:
        print(f"Port {str(port)} IS Closed")
    except UnicodeDecodeError:
        print(f"Port {str(port)} IS Unclear")
    except KeyboardInterrupt:
        print("; You Exit With Type CTRL C OR You Skip Scan")
        
print("Gunakan opsi (,) atau (-) ex : 21,22,80,etc.. atau 21-80")
target = input("Masukkan Target IP Address : ")
ports = input("Masukkan Port : ")

if ',' in ports:
    portlist = ports.split(',')
    for port in portlist:
        scan(target, int(port))
elif '-' in ports:
    portlist = ports.split('-')
    start = int(portlist[0])
    end = int(portlist[1])
    for port in range(start, end+1):
        scan(target, port)
else:
    scan(target, int(ports))
