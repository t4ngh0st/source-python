import os
import socket

def main():
    target_host = input("Enter Target IP : ")
    target_port = 5555
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((target_host, target_port))
        print(f"[*] Connected To {target_host}:{target_port}")
        print("[*] Type 'exit' To Quit")
        
        while True:
            command = input("Shell >> ")
            if not command:
                continue
            
            client.send(command.encode('utf-8'))
            
            if command.lower() == 'exit':
                break
            
            # Accept Output From Target
            response = client.recv(1024).decode('utf-8')
            print(response)
    
    except ConnectionRefusedError:
        print(f"[!] Connection To {target_host}:{target_port} Refused")
    except KeyboardInterrupt:
        print("\n[*] Closing Connection...")
    finally:
        client.close()

if __name__ == "__main__":
    main()