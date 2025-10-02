import socket

user = input("Masukkan DNS(Misalnya: google.com) : ")
ip = socket.gethostbyname(user)
print(f"IP dari {user} : {ip}")
