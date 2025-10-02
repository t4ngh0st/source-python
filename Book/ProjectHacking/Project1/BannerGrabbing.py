import socket

jawab = 'y'

while (jawab =='y'):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    alamat = input("IP Address : ")
    port = input("Port : ")
    result = s.connect_ex((alamat, int(port)))
    if result == 0:
        if port == 80:
            s.send(b'GET / HTTP 1.1\r\n\r\n')
            try:
                banner = s.recv(4096)
                print(banner.decode('ascii'))
            except:
                print("Gagal,Tidak Ada Banner")
            finally:
                s.close()
        else:
            print("Port " + port + "IS Closed")
            s.close()
        jawab = input("Ulangi (y/n)? ")
        if jawab != 'y':
            break