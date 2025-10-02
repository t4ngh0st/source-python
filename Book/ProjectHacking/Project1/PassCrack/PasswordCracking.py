import urllib.request
import urllib.parse

post_url = input("Alamat : ")
# Post URL = 'https://localhost/Efisienser/loginsinggah.php'
jawab ='y'
while(jawab == 'y'):
    username = input("Username: ")
    password = input("Password: ")
    post_data = urllib.parse.urlencode({'username': username,'password': password}).encode('ascii')
    post_response = urllib.request.urlopen(url=post_url, data=post_data)
    print(post_response.info()) # Post Banner Grabber Port 80
    print(post_response.read())
    jawab = input("Ingin Mengulangi Lagi(y/n) : ")
    if jawab != 'y':
        break