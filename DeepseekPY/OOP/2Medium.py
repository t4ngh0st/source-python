# Inheritance & Encapsulation

class Hewan:
    def __init__(self, nama, umur):
        self._nama = nama  # Protected attribute
        self.__umur = umur  # Private attribute
    
    def bersuara(self):
        raise NotImplementedError("Subclass harus mengimplementasikan ini")
    
    def info(self):
        return f"{self._nama} berumur {self.__umur} tahun"
    
    def get_umur(self):
        return self.__umur
    
    def set_umur(self, umur_baru):
        if umur_baru > 0:
            self.__umur = umur_baru
        else:
            print("Umur harus positif")

class Anjing(Hewan):
    def __init__(self, nama, umur, ras):
        super().__init__(nama, umur)
        self.ras = ras
    
    def bersuara(self):
        return f"{self._nama} menggonggong: Guk Guk!"
    
    def info(self):
        return f"{super().info()}, ras {self.ras}"

# Membuat objek
anjing1 = Anjing("Buddy", 5, "Golden Retriever")

print(anjing1.bersuara())  # Output: Buddy menggonggong: Guk Guk!
print(anjing1.info())  # Output: Buddy berumur 5 tahun, ras Golden Retriever

# Mengakses dan mengubah umur melalui method
print(anjing1.get_umur())  # Output: 5
anjing1.set_umur(6)
print(anjing1.get_umur())  # Output: 6