class Dikdortgen:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan_hesapla(self):
        return self.genislik * self.yukseklik

# Kullanım
dikdortgen1 = Dikdortgen(5, 10)
alan = dikdortgen1.alan_hesapla()
print(f"Dikdörtgenin alanı: {alan}")
