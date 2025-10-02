# Sent Message to Server
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5050

message = input("Masukkan Message Untuk UDP >> ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
    print(f"[+] Sent UDP Packet To {UDP_IP}:{UDP_PORT} = '{message}'")

finally:
    sock.close()
