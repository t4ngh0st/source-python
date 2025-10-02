def penambahan():
    a = int(input("Masukkan Nilai a : "))
    b = int(input("Masukkan Nilai b : "))
    return a + b

def pengurangan():
    a = int(input("Masukkan Nilai a : "))
    b = int(input("Masukkan Nilai b : "))
    return a - b

def main():
    while True:
        print("==================")
        print("1. Penambahan")
        print("2. Pengurangan")
        print("3. Exit")
        print("==================")

        user = int(input("Masukkan Nomor : "))

        if user == 3:
            print("Bye Bye")
            exit()
        elif user == 2:
            hasil = penambahan()
            print(f"Hasil = {hasil}")
        elif  user == 1:
            hasil = pengurangan()
            print(f"Hasil = {hasil}")
        else:
            print("Error")

if __name__ == "__main__":
    main()
