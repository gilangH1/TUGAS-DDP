# Gempa.py

class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 3.0:
            print(f"Gempa di {self.lokasi} dengan skala {self.skala} gempa tidak berasa.")
        elif 3.0 <= self.skala < 5.0:
            print(f"Gempa di {self.lokasi} dengan skala {self.skala} dampak gempa bangunan retak retak.")
        elif 5.0 <= self.skala < 7.0:
            print(f"Gempa di {self.lokasi} dengan skala {self.skala} dampak gempa bangunan roboh.")
        else:
            print(f"Gempa di {self.lokasi} dengan skala {self.skala} dampak gempa banunan roboh dan berpotensi tsunami.")