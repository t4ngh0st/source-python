# TCP Client Server
# import socket

# Host = "www.google.com"
# Port = 80

# # Create a Socket
# TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # Connect TCP
# TCP.connect((Host, Port))
# # Send Data 
# TCP.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')

# # Catch Response
# res = TCP.recv(4096)
# print(res.decode())

# TCP.close()

# Custom Own
import socket

print("Port 80 Only !!!")
Host = input("Enter Host: ")
Port = 80

# Create a Socket
Net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect TCP
Net.connect((Host, Port))
# Send Data
Net.send(b'GET / HTTP/1.1\r\nHost : ' + Host.encode() + b'\r\n\r\n')

# Catch Response
res = Net.recv(4096)
print(res.decode())

# Note:
# Host.encode(): Ini adalah bagian pentingnya. Variabel Host awalnya berupa string biasa.
# Untuk bisa digabungkan dengan byte string (b'...'), kita harus mengubah Host menjadi byte juga.
# Fungsi .encode() akan melakukan hal ini, mengubah string menjadi urutan byte.