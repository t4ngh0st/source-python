import socket
import requests
import pprint
import json

hostname = input("Enter a Domain Name : ")
ip_address = socket.gethostbyname(hostname)

API = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(API)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)

for k,v in geolocation.items():
	pprint.pprint(str(k) + ' + ' + str(v))
