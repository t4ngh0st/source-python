# Server UDP Simulation
import socket

# Menentukan IP Address dan Port
UDP_IP = "127.0.0.1"
UDP_PORT = 5050

# Membuat Socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"[+] Listening for UDP Packets on {UDP_IP}:{UDP_PORT}...")

while True:
    try:
        # Menerima data dari socket
        data, addr = sock.recvfrom(1024)  # Fix typo dari "recvrom"
        print(f"[>] Received packet from {addr[0]}:{addr[1]} → '{data.decode('utf-8')}'")
    except KeyboardInterrupt:
        print("\n[!] Listener stopped by user.")
        break
    except Exception as e:
        print(f"[!] Error: {e}")

