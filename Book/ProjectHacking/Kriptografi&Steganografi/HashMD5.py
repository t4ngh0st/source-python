import hashlib

plaintext = input("Nilai Sring > ")
md5 = haslib.md5()
md5.update(plaintext.encode('ascii'))
print("Nilai Hash MD5 : ", md5.hexdigest())
