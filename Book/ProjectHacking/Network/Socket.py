# Modul Ini Berguna Membuat Socket Jaringan Dan Dapat Digunakan Untuk Megetes Terbuka
# Suatu Port Jaringan Atau Tidak Sehingga Dapat Digunakan Untuk Membuat Port Scanner.
# Contoh Script Menggunakan Koneksi TCP:

import socket

# Create A New Socket Using The Given Address Family

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Setting Up The Default TimeOit In Seconds For New Socket Object
socket.setdefaulttimeout(1)
addr = "127.0.0.1"  # IP Address Target,Dapat Diketahui Dari Hasil Ping

port = 80

result = s.connect_ex((addr, port))
if result == 0:
    print("Port {} is open".format(port))
else:
    print("Port {} is closed".format(port))
s.close()

# Setelah Socket Selesai Digunakan,Socket Harus Di Close Untuk Membebaskan Memory
# Penggunaan Socket. SOCK_STREAM Menunjukkan Koneksi TCP, Jika Menginginkan UDP Maka
# SOCK_STREAM Diganti Dengan SOCK_DGRAM.Berikut Contoh Code TCP Port Scanner Dengan
# Menggunakan Daftar Port Tertentu

# import socket
# 
# socket.setdefaukttimeout(1)
# addr = "127.0.0.1"
# listPort = [20,21,22,23,25,53,79,80,110,137,138,139,443,445,3306]
# 
# for port in listPort:
#   S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#   result = S.connect_ex((addr, int(port)))
#   if result == 0:
#       print("Port IS Open " + str(port))
#       S.close()
#   else:
#       print("Port IS Closed " + str(port))
#       S.close()


# Port Service Name

# 20      FTP Data Transfer
# 21      FTP Control Transfer
# 22      SSH
# 23      Telnet
# 25      Simple Mail Transfer Protocol(SMTP atau E-Mail)
# 53      DNS
# 79      FIngerprint
# 80      HTTP
# 110     POP3
# 137     NetBIOS Name Service
# 138     NetBIOS DataGram
# 139     NetBIOS Session Service/Windows Shares
# 443     HTTPS
# 445     Microsoft-DS/Windows Shares
# 3306    MySQL



# <[Server Side Scripting Menggunakan Socket]>
# Modul Socket ini Juga Dapat Digunakan Untuk Membuat Aplikasi Client-Server.
# Script Server Dijalankan Terlebih Dahulu DariPada Script Client.
# Berikut Contoh Script Server:

# import socket

# s = socket.socket()
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))
# s.listen(5)
# while True:
#     c, addr = s.accept()
#     print('Got connection from', addr)
#     c.send('Thank you for connecting')
#     c.close()

# Metode Yang Digunakan Script Server:
# socket.bind()   : Untuk Menandai Alamat(Host dan Port) Dengan Socket
# socket.listen() : Untuk Mendengarkan Hubungan Yang Dibuat Socket,Nilai Minimumnya
# Adalah 0 dan Nilai Maksimum Adalah 5
# socket.accept() : Untuk Menerima Hubungan Dari TCP Client.Metode ini Digunakan Setelah Penggunaan socket.bind() dan socket.listen()


# Berikut Contoh Script Client:
# import socket

# s = socket.socket()
# host = socket.gethostname() # Mendapatkan Nama Mesin Lokal

# # Contoh Penggunaan IP,Host="134.0.0.32"
# port = 1234
# s.connect((host, port))
# print(s.recv(1024))
# s.close()

# Note :
# Cliet Hanya Menggunakan Satu Metode,Yaitu: socket.connect,Yang Berguna Menghubungkan
# Dengan Server,Metode Umum Yang Sering Digunakan Baik Client Atau Server Adalah:
# - socket.recv(bufsize): Metode ini Menerima Peasn TCP dari socket.
# Argumen buffer size Adalah Ukuran Data Yang Dapat DiTerima Pada Satuan Waktu
# - socket.send(bytes): Metode ini Mengirim Data TCP Ke Socket Yang Terkoneksi Dengan
# Mesin Remote.Nilai bytes Argumen Adalah Jumlah byte Yang Dikirim Ke Socket.
# - socket.recvfrom(data, address): Metode ini Menerima Pesan UDP Dari Socket.Ada Dua
# Nilai Yang Dikembalikan,Yaitu Data & Alamat Pengirim Data Ke Socket.
# - socket.sendto(data, address): Metode ini Mengirim Pesan UDP Ke Socket.Dua Nilai Yang
# Dikembalikan Yaitu Data Jumlah Byte Yang Dikirm & Alamat Mesin Yang Di Remote.
# - socket.close(): Metode ini Untuk Menutup Socket.
# - socket.gethostname(): Metode ini Untuk Mendapatkan Nama Host
# - socket.sendall(data): Metode ini Mengirim Semua Data ke Socket Yang Terhubung Dengan
# Mesin Remote.Jika Terjadi Kesalahan Pengirim Maka Digunakan Metode Socket.close().

# Contoh Script Python Untuk Mengirim Pesan Dari Server Ke Client
# Script Server:

# import socket

# def main():
#     host = socket.gethostname()
#     port = 5000
#     server_socket = socket.socket()
#     server_socket.bind((host, port))
#     server_socket.listen(2)
#     print("Socket Sedang Listening")
#     while True:
#         conn, address = server_socket.accept()
#         print("Mendapatkan Koneksi Dari: %s" % str(address))
#         msg = 'Dari Server : Koneksi Sedang Berlangsung' + '\r\n'
#         conn.send(msg.encode('ascii'))
#         conn.close()

# if __name__ == '__main__':
#     main()

# Script Client Server:

# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
# port = 5000
# s.connect((host, port))
# msg = s.recv(1024)
# s.close()
# print(msg.decode('ascii'))

# Pesan Yang Akan Dikirim Sebelumnya Harus DiEncode Dahulu Dengan Perintah Enco
# ('asci) & Saat Akan Diterima Harus DiEncode Dengan Perintah Decode('ascii) supaya
# Dapat Dibaca Kembali