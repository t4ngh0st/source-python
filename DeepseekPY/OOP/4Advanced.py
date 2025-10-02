# Multiple Inheritance & Special Methods

class PerangkatElektronik:
    def __init__(self, merek, daya):
        self.merek = merek
        self.daya = daya  # dalam watt
        self.nyala = False
    
    def hidupkan(self):
        if not self.nyala:
            self.nyala = True
            print(f"{self.merek} dihidupkan")
        else:
            print(f"{self.merek} sudah hidup")
    
    def matikan(self):
        if self.nyala:
            self.nyala = False
            print(f"{self.merek} dimatikan")
        else:
            print(f"{self.merek} sudah mati")
    
    def __str__(self):
        return f"{self.merek} - Daya: {self.daya}W - Status: {'Hidup' if self.nyala else 'Mati'}"

class PerangkatAudio:
    def __init__(self, volume=50):
        self.volume = volume
    
    def naikkan_volume(self, nilai=5):
        self.volume = min(100, self.volume + nilai)
        print(f"Volume dinaikkan menjadi {self.volume}")
    
    def turunkan_volume(self, nilai=5):
        self.volume = max(0, self.volume - nilai)
        print(f"Volume diturunkan menjadi {self.volume}")

class SpeakerBluetooth(PerangkatElektronik, PerangkatAudio):
    def __init__(self, merek, daya, koneksi=False):
        PerangkatElektronik.__init__(self, merek, daya)
        PerangkatAudio.__init__(self)
        self.koneksi = koneksi
    
    def sambungkan(self):
        if not self.koneksi:
            self.koneksi = True
            print(f"{self.merek} tersambung via Bluetooth")
        else:
            print(f"{self.merek} sudah tersambung")
    
    def putuskan(self):
        if self.koneksi:
            self.koneksi = False
            print(f"{self.merek} terputus dari Bluetooth")
        else:
            print(f"{self.merek} sudah terputus")
    
    def __str__(self):
        status_elektronik = super().__str__()
        return f"{status_elektronik} - Koneksi: {'Terhubung' if self.koneksi else 'Terputus'} - Volume: {self.volume}"

# Membuat objek
speaker = SpeakerBluetooth("JBL", 20)

print(speaker)  # Output: JBL - Daya: 20W - Status: Mati - Koneksi: Terputus - Volume: 50

speaker.hidupkan()
speaker.sambungkan()
speaker.naikkan_volume(15)

print(speaker)  # Output: JBL - Daya: 20W - Status: Hidup - Koneksi: Terhubung - Volume: 65

# Demonstrasi operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)  # Output: Vector(6, 8)
print(v2 - v1)  # Output: Vector(2, 2)
print(v1 * 3)   # Output: Vector(6, 9)