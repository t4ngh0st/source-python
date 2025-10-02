import requests

response = requests.get('https://api.github.com')
if response.status_code == 200:
    print('Success!')
else:
    print('Error:', response.status_code)