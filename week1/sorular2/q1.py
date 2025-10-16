class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas
    
    def konus(self):
        print(f"Merhaba, ben {self.ad}.")

class Hoca(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)
        self.sicil_no = sicil_no
    
    def konus(self):
        print(f"Merhaba, ben {self.ad}, bir öğretmenim.")
    
    def ders_ver(self):
        print(f"{self.ad} ders veriyor.")

class Sekreter(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)
        self.sicil_no = sicil_no
    
    def konus(self):
        print(f"Merhaba, ben {self.ad}, sekreterim.")
    
    def randevu_al(self):
        print(f"{self.ad} randevu alıyor.")

class Ogrenci(Insan):
    def __init__(self, ad, yas, ogrenci_no):
        super().__init__(ad, yas)
        self.ogrenci_no = ogrenci_no
    
    def konus(self):
        print(f"Merhaba, ben {self.ad}, öğrenciyim.")
    
    def ders_dinle(self):
        print(f"{self.ad} ders dinliyor.")

# Kullanım örneği
hoca1 = Hoca("Ahmet", 45, "H123")
sekreter1 = Sekreter("Ayşe", 30, "S456")
ogrenci1 = Ogrenci("Mehmet", 20, "2021001")

hoca1.konus()
hoca1.ders_ver()

sekreter1.konus()
sekreter1.randevu_al()

ogrenci1.konus()
ogrenci1.ders_dinle()