import hashlib

plaintext = input("Nilai String : ")
sha = hashlib.sha1()
sha.update(plaintext.encode('ascii'))
print("Nilai Hash Sha1 : ", sha.hexdigest())