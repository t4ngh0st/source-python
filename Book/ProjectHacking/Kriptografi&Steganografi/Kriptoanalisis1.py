z =['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print("== Sandi Geser ==")

a = input("\nMasukkan Kata >> ")
b = ""
geser = 7

for x in range(len(a)):
    temp = z.index(a[x]) + geser
    b = b + z[temp % 63] + b
    
print("\nPlainText = " + a)
print("CipherText = " + b)