#                        == Tabel ==
# Operator          Makna                       Contoh          Hasil
# ========================================================================
#    ==         Sama Dengan                     x == y          FALSE
# != atau <>    Tidak Sama Dengan               x != y          TRUE
#    <          Lebih Kecil Dari                x < y           TRUE
#    >          Lebih Besar Dari                x > y           FALSE
#    <=         Lebih Kecil/Sama Dengan Dari    x <= y          TRUE
#    >=         Lebih Besar/Sama Dengan Dari    x >= y          FALSE


# Mengambil Input User
a = int(input("Masukkan Nilai a >> "))
b = int(input("Masukkan Nilai b >> "))

print("\nOpertor ==")
if(a==b):
    print("- Nilai a Sama Dengan b\n")
else:
    print("- Nilai a Tidak Sama Dengan b\n")

print("Operator != atau <>")
if(a!=b):
    print("- Nilai a TIdak Sama Dengan b\n")
else:
    print("- Nilai a Sama Dengan b\n")
    
print("Operator <")
if(a<b):
    print("- Nilai a Lebih Kecil Dari b\n")
else:
    print("- Nilai a Lebih Besar Dari b\n")
    
print("Operator >")
if(a>b):
    print("- Nilai a Lebih Besar Dari b\n")
else:
    print("- Nilai a Lebih Kecil Dari b\n")
    
print("Operator <=")
if(a<=b):
    print("Nilai a Lebih Kecil/Sama Dengan Dari b\n")
else:
    print("Nilai a Lebih Besar/Sama Dengan Dari b\n")

print("Operator >=")
if(a>=b):
    print("Nilai a Lebih Besar/Sama Dengan Dari b\n")
else:
    print("Nilai a Lebih Kecil/Sama Dengan Dari b\n")