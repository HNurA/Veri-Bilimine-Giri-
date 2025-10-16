class Kare:
    def __init__(self, kenar):
        self.kenar = kenar

    def kareyi_yazdir(self):
        for i in range(self.kenar):
            print("* " * self.kenar)

# Kare sınıfından bir nesne oluşturma ve kareyi yazdırma
kare1 = Kare(5)
kare1.kareyi_yazdir()
