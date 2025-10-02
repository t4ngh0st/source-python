# Polymorphism & Class Methods

from math import pi
from datetime import datetime

class Bentuk:
    def __init__(self, nama):
        self.nama = nama
    
    def luas(self):
        pass
    
    def keliling(self):
        pass
    
    def info(self):
        return f"Ini adalah {self.nama} dengan luas {self.luas():.2f} dan keliling {self.keliling():.2f}"
    
    @classmethod
    def buat_dari_input(cls):
        nama = input(f"Masukkan nama {cls.__name__}: ")
        return cls(nama)

class Lingkaran(Bentuk):
    def __init__(self, nama, radius):
        super().__init__(nama)
        self.radius = radius
    
    def luas(self):
        return pi * self.radius ** 2
    
    def keliling(self):
        return 2 * pi * self.radius
    
    @classmethod
    def buat_dari_input(cls):
        nama = input("Masukkan nama lingkaran: ")
        radius = float(input("Masukkan radius: "))
        return cls(nama, radius)

class Persegi(Bentuk):
    def __init__(self, nama, sisi):
        super().__init__(nama)
        self.sisi = sisi
    
    def luas(self):
        return self.sisi ** 2
    
    def keliling(self):
        return 4 * self.sisi
    
    @classmethod
    def buat_dari_input(cls):
        nama = input("Masukkan nama persegi: ")
        sisi = float(input("Masukkan panjang sisi: "))
        return cls(nama, sisi)

class LogAktivitas:
    log_aktivitas = []
    
    @classmethod
    def tambah_log(cls, aktivitas):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cls.log_aktivitas.append(f"{waktu} - {aktivitas}")
    
    @classmethod
    def tampilkan_log(cls):
        print("\nLog Aktivitas:")
        for log in cls.log_aktivitas:
            print(log)

# Demonstrasi polymorphism
bentuk1 = Lingkaran("Lingkaran Besar", 10)
bentuk2 = Persegi("Kotak Kecil", 5)
bentuk3 = Lingkaran.buat_dari_input()  # Membuat dari input user

bentuk_list = [bentuk1, bentuk2, bentuk3]

for bentuk in bentuk_list:
    print(bentuk.info())  # Setiap objek merespon berbeda terhadap method yang sama

# Menggunakan class method untuk logging
LogAktivitas.tambah_log("Program dijalankan")
LogAktivitas.tambah_log("Lingkaran dibuat")
LogAktivitas.tambah_log("Persegi dibuat")
LogAktivitas.tampilkan_log()