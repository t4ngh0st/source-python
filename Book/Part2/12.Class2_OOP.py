class Makanan:
    __about = "Created By Muhammad Luthfi Fakhmar"
    __menu = ""
    nama = ""
    def __init__(self, nama):
        self.nama = nama
    def get_about(self):
        print(self.__about)
        print("Yang Dipilih : %s" % self.__menu)
    def set_food(self, isian):
        if isian == 'sate':
            print("Sate Enak Tapi Kolestrol Tinggi")
        elif isian == 'nasi goreng':
            print("Nasi Goreng Enak Juga")
        elif isian == 'ayam goreng':
            print("Murah Meriah dan Enak")
        else:
            print("No Comment")
        self.__menu = isian
        
m = Makanan("siang")
m.set_food("sate")
m.get_about()