from collections import deque
import re
from bs4 import BeautifulSoup
import requests
import urllib.parse

user_url = input("[+] Masukkan URL >> ")
urls = deque([user_url])
scraped_urls = set()
emails = set()
count = 0
limit = int(input("[+] Masukkan Batas Pencarian >> "))

try:
    while urls:  # Lanjutkan selama masih ada URL dalam antrian
        count += 1
        if count > limit:
            break

        url = urls.popleft()
        scraped_urls.add(url)
        parts = urllib.parse.urlsplit(url)
        base_url = f'{parts.scheme}://{parts.netloc}'
        path = url[:url.rfind('/') + 1] if '/' in parts.path else base_url  # Gunakan base_url jika tidak ada '/' di path

        print(f'[+]{count} Memproses... {url}')

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.RequestException) as e:
            print(f"[-] Gagal mengambil URL: {url} - {e}")
            continue

        new_emails = set(re.findall(r'[a-z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-zA-Z]+', response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, 'html.parser')
        for anchor in soup.find_all('a'):
            link = anchor.get('href', '')  # Gunakan .get() untuk menghindari AttributeError jika 'href' tidak ada
            if link.startswith('/'):
                link = urllib.parse.urljoin(base_url, link)
            elif not link.startswith('http'):
                link = urllib.parse.urljoin(path, link)

            if link not in urls and link not in scraped_urls:
                urls.append(link)

except KeyboardInterrupt:
    print("[-] Menghentikan pemrosesan!")

print('\n[+] Proses Selesai')
print(f'\n[+] {len(emails)} E-mail Ditemukan!!! \n{"="*35}')

for mail in emails:
    print(' ' + mail)
print('\n')
