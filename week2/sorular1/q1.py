# 1. İnsan Sınıfı
class Insan:
    def __init__(self, isim, yas, cinsiyet):
        self.isim = isim
        self.__yas = yas  # Private (gizli) özellik
        self.cinsiyet = cinsiyet
    
    def bilgi_ver(self):
        print(f"İsim: {self.isim}, Yaş: {self.__yas}, Cinsiyet: {self.cinsiyet}")
    
    # Getter ve Setter metodları
    def get_yas(self):
        return self.__yas
    
    def set_yas(self, yeni_yas):
        if yeni_yas > 0:
            self.__yas = yeni_yas
        else:
            print("Yaş pozitif olmalıdır!")


# 2. Hoca Sınıfı (Insan'dan miras alır)
class Hoca(Insan):
    def __init__(self, isim, yas, cinsiyet, brans):
        super().__init__(isim, yas, cinsiyet)
        self.brans = brans
    
    def konus(self):
        return f"{self.isim} adlı hoca {self.brans} dersini anlatıyor."


# 3. Öğrenci Sınıfı (Insan'dan miras alır)
class Ogrenci(Insan):
    def __init__(self, isim, yas, cinsiyet, sinif, okul_no):
        super().__init__(isim, yas, cinsiyet)
        self.sinif = sinif
        self.__okul_no = okul_no  # Private (gizli) özellik
    
    def konus(self):
        return f"{self.isim} adlı öğrenci derste konuşuyor."
    
    def katil(self):
        return f"{self.isim} adlı öğrenci {self.sinif} sınıfında derse katılıyor."
    
    # Getter ve Setter metodları
    def get_okul_no(self):
        return self.__okul_no
    
    def set_okul_no(self, yeni_no):
        if yeni_no > 0:
            self.__okul_no = yeni_no
        else:
            print("Okul numarası pozitif olmalıdır!")


# 4. Ana Program
print("=== İNSAN NESNESİ ===")
insan1 = Insan("Ali", 40, "Erkek")
insan1.bilgi_ver()
print(f"Yaş (getter ile): {insan1.get_yas()}")

print("\n=== HOCA NESNESİ ===")
hoca1 = Hoca("Ayşe", 35, "Kadın", "Matematik")
hoca1.bilgi_ver()
print(hoca1.konus())  # Polimorfizm

print("\n=== ÖĞRENCİ NESNESİ ===")
ogrenci1 = Ogrenci("Mehmet", 18, "Erkek", "12-A", 2021001)
ogrenci1.bilgi_ver()
print(ogrenci1.konus())  # Polimorfizm
print(ogrenci1.katil())
print(f"Okul No (getter ile): {ogrenci1.get_okul_no()}")

print("\n=== SETTER KULLANIMI ===")
ogrenci1.set_yas(19)
ogrenci1.set_okul_no(2021002)
print(f"Yeni Yaş: {ogrenci1.get_yas()}")
print(f"Yeni Okul No: {ogrenci1.get_okul_no()}")

print("\n=== POLİMORFİZM ÖRNEĞİ ===")
kisiler = [hoca1, ogrenci1]
for kisi in kisiler:
    print(kisi.konus())  # Aynı metot ismi, farklı davranışlar