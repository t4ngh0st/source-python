def show_menu():
    print("\n===== Menu =====")
    print("[1] Show Data")
    print("[2] Add Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    print("================\n")
    
    user = int(input("[?] Masukkan Opsi >> "))
    print(" ")
    
    if user == 5:
        print("Bye Bye...")
        exit()
    elif user == 1:
        print("Show Data")
    elif user == 2:
        print("Add Data")
    elif user == 3:
        print("Edit Data")
    elif user == 4:
        print("Delete Data")
    else:
        print("Error")

# Menjalankan program utama jika skrip ini dieksekusi langsung
if __name__ == "__main__":
    show_menu()