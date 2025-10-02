# OOP : Class & Basic Object

class Kucing:
    # Constructor method (spesial method __init__)
    def __init__(self, nama, umur):
        self.nama = nama # Atribut instance
        self.umur = umur # Atribut instance
    
    # Method instance
    def meong(self):
        return f"{self.nama} meow meow"
    def info(self):
        return f"{self.nama} berumur {self.umur} tahun"

# Membuat Objek
kucing1 = Kucing("Tom", 3)
kucing2 = Kucing("Jerry", 2)

# Mengakses Atribut & Method
print(kucing1.nama)     # Output : Tom
print(kucing2.meong())   # Output : Jerry meow meow
print(kucing1.info())   # Output : Tom berumur 3 tahun))


