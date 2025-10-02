import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Function succesfully created")
except socket.error as err:
    print("Socket creation failed with error %s" %(err))

# default port for socket
port = 80

try:
    user = input("Masukkan DNS(Misalnya: google.com): ")
    host = socket.gethostbyname(user)
except socket.gaierror:
    pass

    print("Error Host")
    sys.exit()

# Connection to the server

s.connect((host, port))
print(f"Socket berhasil terhubung dengan {user} : {port}")
print(f"IP : {host}")
