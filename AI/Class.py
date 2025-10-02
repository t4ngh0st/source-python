class Orang:
    def __init__(self, nama):
        self.nama = nama

    def katakan_halo(self):
        print("Nama saya %s, apa kabar?" % self.nama)

rudi = Orang('rudi')
rudi.katakan_halo()
