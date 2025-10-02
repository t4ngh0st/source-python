import os

def clear():
    if os.name == 'win32':
        x = os.system('cls')
    elif os.name == 'linux':
        x = os.system('clear')
    elif os.name == 'darwin':
        x = os.system('clear')
    else:
        print("What's Your Operation System?")

def Loop():
    jawab = ""
    while(jawab == ""):
        user = input("Do You Want Repeat Again?(Y/n) : ")
        if user == "":
            clear()
            main()
        elif user in ['n', 'N', 'no', 'No']:
            print("Your Exit")
            exit()
        else:
            print("What Do You Choose!...")
            exit()

def create():

def delete():

def update():

def search():

def List():


def main():
    print("===== SPP =====")
    print("[1] Create     ")
    print("[2] Delete     ")
    print("[3] Update     ")
    print("[4] Search     ")
    print("[5] List       ")
    print("[6] Exit       ")
    print("===============")
    
    user = int(input("Choose Number : "))
    
    