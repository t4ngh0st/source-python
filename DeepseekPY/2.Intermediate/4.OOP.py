class Hewan:
    def __init__(self, nama, spesies):
        self.nama = nama
        self.spesies = spesies
        
    def bersuara(self):
        print("...")
        
class Kucing(Hewan):
    def __init__(self, nama, warna):
        super().__init__(nama, "Felis Catus")
        self.warna = warna
    
    def bersuara(self):
        print("Meong!")
        
kucing1 = Kucing("Tom", "Abu-abu")
kucing1.bersuara()