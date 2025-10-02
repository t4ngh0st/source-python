import test

def show_menu():
    print("===== Menu =====")
    print("[1] SegiEmpat")
    print("[0] Exit")
    print("=================")
    
    user = int(input("Input Pilihan >> "))
    
    if user == 1:
        test.segiempat()
    elif user == 0:
        exit
    else:
        print("error")

if __name__ == "__main__":
    show_menu()
    jawab = ""
    while(jawab == ""):
        jawab = input("\nUlangi Lagi?(Y/n) >> ")
        if jawab == "":
            show_menu()
        elif jawab == "n":
            break