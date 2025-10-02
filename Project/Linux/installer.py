import os
# 'posix' : Linux & MacOS
# 'nt'    : windows

# win32   : Windows
# linux   : Linux
# darwin  : Mac Os

def clear():
    if os.name == 'posix':
        x = os.system("clear")
    else:
        x = os.system("cls")

def again():
    while True:
        try:
            user_choice = input("Return to Main Menu (Y/n)? ").strip()
            user_choice_lower = user_choice.lower()
            if user_choice == "" or user_choice_lower in ['Y', 'y', 'Yes', 'yes', 'Ya', 'ya']:
                mainMenu()
            elif user_choice_lower in ['N', 'n', 'No', 'no','T', 't','Tidak', 'tidak']:
                print("\nBye Bye Bye ...\n")
                exit()
            else:
                print(f"Input {user} Insvalid")
                exit()
        except (KeyboardInterrupt, EOFError): # Menangani CTRL + C & CTRL + D
            print("\nBye Bye Bye ...\n")
            exit()
        except Exception as e: # Menangani Error Yang Lain
            print(f"\nAn Unexpected Error Occurred: {e}.Program Will Exit Now\n")
            exit()

def Info():
    clear()
    print("\n===== Tools =====")
    print("[1] TheHarvester")
    print("[2] Whois")
    print("[3] Nslookup")
    print("[4] Recon-Ng")
    print("[5] Sublist3r")
    print("[6] Amass")
    print("[7] Maltego")
    print("[8] Discover")
    print("[9] Netdiscover")
    print("[10] Spiderfoot")
    print("[11] Websploit")
    print("[12] Dmitry")
    print("[13] Exit")
    print("[00] Back")
    print("=================\n")
    
    user = int(input("Choose Number >> "))
    
    if user == 1:
        print("Installing TheHarvester....")
        return_code = os.system("sudo apt install theharvester -y")
        if return_code == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {return_code}\n")
            again()
    
    elif user == 2:
        print("Installing Whois.....")
        i = os.system("sudo apt install whois -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 3:
        print("Installing Nslookup.....")
        i = os.system("sudo apt install nslookup -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError Installing,Command Returned Exit Code: {i}\n")
            again()
            # print("Trying to install with 'sudo apt install bind9-dnsutils'...\n")
            
        # New Var
        # j = os.system("sudo apt install bind9-dnsutils -y")
        # if j == 0:
        #     print("\nNslookup(Via bind9-dnsutils) Installed Successfully")
        # else:
        #     print(f"\nError installing Whois. Command returned exit code: {j}")
    
    elif user == 4:
        print("Installing Recon-Ng.....")
        i = os.system("sudo apt install recon-ng -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 5:
        print("Installing Sublist3r.....")
        i = os.system("sudo apt install sublist3r -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 6:
        print("Installing Amass.....")
        i = os.system("sudo apt install amass -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()

    elif user == 7:
        print("Installing Maltego.....")
        i = os.system("sudo apt install maltego -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 8:
        print("Cloning Discover From Github : https://github.com/cyberconsultant3199/OSINT-discover.git")
        i = os.system("git clone https://github.com/cyberconsultant3199/OSINT-discover.git")
        j = os.system("cd OSINT-discover")
        b = os.system("sudo chmod +x *")
        v = os.system("./update.sh")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print("\nError installing. Command returned exit code: {i}\n")
            again()
        
    elif user == 9:
        print("Installing Netdiscover.....")
        i = os.system("sudo apt install netdiscover -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError Installing. Command returned exit code: {i}\n")
            again()
            
    elif user == 10:
        print("Installing Spiderfoot.....")
        i = os.system("sudo apt install spiderfoot -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError Installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 11:
        print("Installing Websploit.....")
        i = os.system("sudo apt install websploit -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError Installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 12:
        print("Installing Dmitry.....")
        i = os.system("sudo apt install dmitry -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError Installing. Command returned exit code: {i}\n")
            again()

    elif user == 13:
        print("\nBye Bye Bye ...\n")
        exit()
    
    elif user == 00:
        mainMenu()
    
    else:
        print("\nSystem Error\n")
        again()

def Vul():
    clear()
    print("\n===== Tools =====")
    print("[1] OpenVAS/GVM")
    print("[2] Burpsuite")
    print("[3] OWASP Zap")
    print("[4] Nikto")
    print("[5] Nuclei")
    print("[6] Exit")
    print("[0] Back")
    print("=================\n")
    
    user = int(input("Choose Number >> "))
    
    if user == 1:
        print("Installing GVM.....")
        i = os.system("sudo apt install gvm -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing GVM. Command returned exit code: {i}\n")
            again()
    
    elif user == 2:
        print("Installing Burpsuite.....")
        i = os.system("sudo apt install burpsuite -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing Burpsuite. Command returned exit code: {i}\n")
            again()
            
    elif user == 3:
        print("Installing OWASP Zap.....")
        i = os.system("sudo apt install zaproxy -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing OWASP Zap. Command returned exit code: {i}\n")
            again()
            
    elif user == 4:
        print("Installing Nikto.....")
        i = os.system("sudo apt install nikto -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
            
    elif user == 5:
        print("Installing Nuclei.....")
        i = os.system("sudo apt install nuclei -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
            
    elif user == 6:
        print("\nBye Bye Bye...\n")
        exit()
    
    elif user == 0:
        mainMenu()
    
    else:
        print("\nSytem Error\n")
        again()
    
def Net():
    clear()
    print("\n===== Tools =====")
    print("[1] NMAP")
    print("[2] Masscan")
    print("[3] Hping3")
    print("[4] Netcat")
    print("[5] Enum4linux")
    print("[6] Legion")
    print("[7] Exit")
    print("[0] Back")
    print("=================\n")
    
    user = int(input("Choose Number >> "))
    
    if user == 1:
        print("Installing Nmap....")
        return_code = os.system("sudo apt install nmap -y")
        if return_code == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {return_code}\n")
            again()
    
    elif user == 2:
        print("Installing Amass.....")
        i = os.system("sudo apt install masscan -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 3:
        print("Installing Hping3.....")
        i = os.system("sudo apt install hping3 -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 4:
        print("Installing Netcat.....")
        i = os.system("sudo apt install netcat-traditional -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing Netcat. Command returned exit code: {i}\n")
            again()
    
    elif user == 5:
        print("Installing Enum4linux.....")
        i = os.system("sudo apt install enum4linux -y")
        if i == 0:
            print("\nEnum4linux Installed Successfully\n")
            again()
        else:
            print(f"\nError installing Enum4linux. Command returned exit code: {i}\n")
            again()
    
    elif user == 6:
        print("Installing Legion.....")
        i = os.system("sudo apt install legion -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing Legion. Command returned exit code: {i}\n")
            again()
    
    elif user == 7:
        print("\nbye bye bye...\n")
    
    elif user == 0:
        mainMenu()
    
    else:
        print("\nSystem Error\n")
        again()
    
    
def Ex():
    clear()
    print("\n======= Tools =======")
    print("[1] Metasploit")
    print("[2] SQL Map")
    print("[3] Searchploit")
    print("[4] Hydra")
    print("[5] John The Ripper")
    print("[6] Hashcat")
    print("[7] Commix")
    print("[8] Setoolkit")
    print("[9] Powershell")
    print("[10] Exit")
    print("[00] Back")
    print("=====================\n")
    
    user = int(input("Choose Number >> "))
    
    if user == 1:
        print("Installing Metasploit.....")
        i = os.system("sudo apt install metasploit-framework -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing Metasploit. Command returned exit code: {i}\n")
            again()
    
    elif user == 2:
        print("Installing SQL Map.....")
        i = os.system("sudo apt install sqlmap -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 3:
        print("Installing Searchploit.....")
        i = os.system("sudo apt install exploitdb -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing Searchploit. Command returned exit code: {i}\n")
            again()
    
    elif user == 4:
        print("Installing Hydra.....")
        i = os.system("sudo apt install hydra-y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 5:
        print("Installing John The Ripper.....")
        i = os.system("sudo apt install john -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 6:
        print("Installing hashcat.....")
        i = os.system("sudo apt install hashcat -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 7:
        print("Installing Commix.....")
        i = os.system("sudo apt install commix -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 8:
        print("Installing Setoolkit.....")
        i = os.system("sudo apt install set -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 9:
        print("Installing Powershell.....")
        i = os.system("sudo apt install powershell -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 10:
        print("\nBye Bye Bye...\n")
        exit()
    
    elif user == 00:
        mainMenu()
    
    else:
        print("\nSystem Error\n")
        again()
        
    
def Web():
    clear()
    print("\n=========== Tools ===========")
    print("[1] Burpsuite")
    print("[2] OWASP Zap")
    print("[3] Brute Force Dictionary")
    print("[4] Wfuzz")
    print("[5] Nikto")
    print("[6] Parsero")
    print("[7] Exit")
    print("[0] Back")
    print("=============================\n")
    
    user = int(input("Choose Number >> "))
    
    if user == 1:
        print("Installing Burpsuite.....")
        i = os.system("sudo apt install burpsuite -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 2:
        print("Installing OWASP Zap.....")
        i = os.system("sudo apt install zaproxy -y")
        if i == 0:
            print("\n\Installed Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 3:
        print("Installing Brute Force Dictionary(Dirb,Dirbuster & Gobuster).....")
        i = os.system("sudo apt install dirb dirbuster gobuster -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 4:
        print("Installing Wfuzz.....")
        i = os.system("sudo apt install wfuzz -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 5:
        print("Installing Nikto.....")
        i = os.system("sudo apt install nikto -y")
        if i == 6:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 6:
        print("Installing Parsero.....")
        i = os.system("sudo apt install parsero -y")
        if i == 6:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 7:
        print("\nBye Bye Bye\n")
        exit()
    
    elif user == 0:
        mainMenu()
        
    else:
        print("\nSystem Error\n")
        again()
    
def Pass():
    clear()
    print("\n======= Tools =======")
    print("[1] John The Ripper")
    print("[2] Hascat")
    print("[3] Ophcrack")
    print("[4] Exit")
    print("[0] Back")
    print("=====================\n")
    
    user = int(input("Choose Number >> "))
    
    if user == 1:
        print("Installing John The Ripper.....")
        i = os.system("sudo apt install john -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 2:
        print("Installing Hashcat.....")
        i = os.system("sudo apt install hashcat -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 3:
        print("Installing Ophcrack.....")
        i = os.system("sudo apt install ophcrack -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 4:
        print("\nBye Bye Bye...\n")
        exit()
    
    elif user == 0:
        mainMenu()
        
    else:
        print("\nSystem Error\n")
        again()
    
def Wire():
    clear()
    print("\n===== Tools =====")
    print("[1] Aircrack-Ng")
    print("[2] Wifite")
    print("[3] Reaver")
    print("[4] Kismet")
    print("[5] MDK3")
    print("[6] EAPHammer")
    print("[7] Exit")
    print("[0] Back")
    print("=================\n")
    
    user = int(input("Choose Number >> "))
    
    if user == 1:
        print("Installing Aircrack-Ng.....")
        i = os.system("sudo apt install aircrack-ng -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 2:
        print("Installing Wifite.....")
        i = os.system("sudo apt install wifite -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 3:
        print("Installing Reaver.....")
        i = os.system("sudo apt install reaver -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 4:
        print("Installing Kismet.....")
        i = os.system("sudo apt install kismet -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 5:
        print("Installing MDK3.....")
        i = os.system("sudo apt install mdk3 -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 6:
        print("Installing EAPHammer.....")
        i = os.system("sudo apt install eaphammer -y")
        if i == 0:
            print("\nInstalled Successfully\n")
            again()
        else:
            print(f"\nError installing. Command returned exit code: {i}\n")
            again()
    
    elif user == 7:
        print("\nBye Bye  Bye...\n")
        exit()
        
    elif user == 0:
        mainMenu()
        
    else:
        print("\nSystem Error\n")
        again()

def mainMenu():
    clear()
    print("\n========== Tools Menu ==========")
    print("[1] Information Gathering")
    print("[2] Vulnerabilty Scanning")
    print("[3] Network Scanning")
    print("[4] Exploitation")
    print("[5] Web Application Testing")
    print("[6] Password Cracking")
    print("[7] Wireless Hacking")
    print("[8] Exit")
    print("================================\n")
    
    user = int(input("Choose Number >> "))
    
    if user == 1:
        Info()

    elif user == 2:
        Vul()

    elif user == 3:
        Net()

    elif user == 4:
        Ex()
    
    elif user == 5:
        Web()
        
    elif user == 6:
        Pass()
        
    elif user == 7:
        Wire()

    elif user == 8:
        print("\nBye Bye Bye ....\n")
        exit()
        
    else:
        print("\nNot Choose in Menu\n")
    

if __name__ == '__main__':
    mainMenu()