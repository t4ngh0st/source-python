# Common Formm 
jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulangi Lagi ?(ya/tidak)")
    if jawab == 'tidak':
        break
print("Total Perulangan : " + str(hitung))
