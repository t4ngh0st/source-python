# Modul Request Berguna Mengambil Source Code Yang Merupakan Respon Permitaan
# GET Dari Suatu Alamat URL(Website)

import requests
req - requests.get('http://Example.com/directory/')
print('\n Response :\n' + req.text)