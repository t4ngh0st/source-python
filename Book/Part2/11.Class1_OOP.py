class Orang:
    def __init__(self, nama):
        self.nama = nama

    def katakan_halo(self):
        print("Nama saya %s, apa kabar?" % self.nama)
        # Menggunakan kelas Orang yang sudah diperbaiki
rudi = Orang('Rudi')
rudi.katakan_halo()
