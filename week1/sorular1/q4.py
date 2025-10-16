class HesapMakinesi:
    def topla(self, sayi1, sayi2, sayi3=None):
        if sayi3 is not None:
            return sayi1 + sayi2 + sayi3
        else:
            return sayi1 + sayi2

# HesapMakinesi sınıfından bir nesne oluşturma
hesap_makinesi = HesapMakinesi()

# İki sayı ile toplama
sonuc1 = hesap_makinesi.topla(10, 20)
print("İki sayının toplamı:", sonuc1)

# Üç sayı ile toplama
sonuc2 = hesap_makinesi.topla(10, 20, 30)
print("Üç sayının toplamı:", sonuc2)
