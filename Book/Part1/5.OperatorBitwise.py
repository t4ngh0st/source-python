#       Nama                    Simbol
# =======================================
#       AND                      &
#        OR                        |
#       XOR                      ^
#   Negasi/Kebalikan               ~
#   Left Shift                  <<
#   Right Shift                    >>

# Variable a = 60 >> 00111100
# Variavle b = 13 >> 00001101

a = int(input("Masukkan Nilai a >> "))
b = int(input("Masukkan Nilai b >> "))

# Operasi AND
c = a & b
print("Operasi AND Bitwise = " + str(c))

# Operasi OR
c = a | b
print("Operasi OR Bitwise = " + str(c))

# Operasi XOR
c = a ^ b
print("Operasi XOR Bitwise = " + str(c))

# Operasi Negasi/Kebalikan
# c = a ^ b
# print("Operasi Negasi/Kebalikan Bitwise = " + str(c))

# Operasi Left Shift
c = a << b
print("Operasi Left Shift Bitwise = " + str(c))

# Operasi Right Shift
c = a >> b
print("Operasi Right Shift Bitwise = " + str(c))
