# Tuples Adalah List Yang Tidak Dapat Diubah(Mongedit,Menambah,Menghapus)
x = 1, 2, 3
print(x[1])
print(x[0:2])

x1 = (1, 2, 3)
print(3*x[1])
print(3*x[0:2])

# >> Tuple
# Isinya Tidak Dapat Diubah(Imutable)
# Isinya Boleh Duplikat

def main():
    print("\nTuple")
    arrayTuple = ("gado-gado", "ketoprak", "Nasi", "Nasi")
    print(arrayTuple)
    print(" ")
    
    for x in arrayTuple:
        print("Daftar Makanan 1: %s" % x)
    print(" ")
main()