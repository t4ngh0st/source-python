# if >> Nilai True
# elif >> Nilai True
# else >> Nilai False

umur = int(input("Masukkan Umur Anda >> "))

if umur > 49:
    print("Kamu Lansia")
elif umur > 19:
    print("Kamu Dewasa")
elif umur > 11:
    print("Kamu Remaja")
elif umur > 9:
    print("Kamu Anak-Anak")
elif umur < 5:
    print("Kamu Balita")
elif umur < 3:
    print("Kamu Bayi")
else:
    print("Kamu Anomali")