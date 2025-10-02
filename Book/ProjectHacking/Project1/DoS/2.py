import socket
import time

alamat = input("IP Address : ")
port = input("Port : ")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
jawab = 'y'

while(jawab == 'y'):
    waktu = time.starttime("%d/%m/%Y, %H", time.localtime())
    if str(waktu) == '08/06/2019, 11':
        try:
            result = s.connect_ex((alamat,int(port)))
            if port == 80:
                s.send(b'GET /HTTP\1.1\r\n\r\n')
                s.send(b"SErang!!!!!!!!!!!!")
        except:
            s.close()
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    else:
        if str(waktu) == '08/06/2019, 12:
        break
        s.close()
exit()