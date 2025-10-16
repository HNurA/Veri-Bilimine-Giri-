from abc import ABC, abstractmethod

# Abstract sınıf - Özgeçmiş
class Ozgecmis(ABC):
    @abstractmethod
    def ozgecmis_goster(self):
        pass

# Ata sınıf - Çalışan
class Calisan(Ozgecmis):
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
    
    def calis(self):
        print(f"{self.ad} çalışıyor.")

# Alt sınıf - Mavi Yaka
class MaviYaka(Calisan):
    def __init__(self, ad, soyad, vardiya=3):
        super().__init__(ad, soyad)
        self.vardiya = vardiya
    
    def calis(self):  # Method Overriding
        print(f"{self.ad} {self.soyad} tezgahta/fabrika içinde çalışıyor. ({self.vardiya} vardiya)")
    
    def ozgecmis_goster(self):  # Abstract metot dolduruldu
        print(f"Özgeçmiş: {self.ad} {self.soyad} - Mavi Yaka Çalışan, {self.vardiya} vardiya sistemi")

# Alt sınıf - Beyaz Yaka
class BeyazYaka(Calisan):
    def __init__(self, ad, soyad, vardiya=2):
        super().__init__(ad, soyad)
        self.vardiya = vardiya
    
    def calis(self):  # Method Overriding
        print(f"{self.ad} {self.soyad} masa başında çalışıyor. ({self.vardiya} vardiya)")
    
    def ozgecmis_goster(self):  # Abstract metot dolduruldu
        print(f"Özgeçmiş: {self.ad} {self.soyad} - Beyaz Yaka Çalışan, {self.vardiya} vardiya sistemi")

# Nesneler oluşturma (Construction)
print("=== MAVİ YAKA ÇALIŞAN ===")
isci1 = MaviYaka("Ahmet", "Yılmaz")
isci1.calis()
isci1.ozgecmis_goster()

print("\n=== BEYAZ YAKA ÇALIŞAN ===")
memur1 = BeyazYaka("Ayşe", "Demir")
memur1.calis()
memur1.ozgecmis_goster()

print("\n=== POLİMORFİZM ÖRNEĞİ ===")
calisanlar = [isci1, memur1]
for calisan in calisanlar:
    calisan.calis()  # Aynı metot ismi, farklı çıktılar