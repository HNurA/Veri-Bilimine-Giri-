class Araba:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgileri_yazdir(self):
        print(f"Marka: {self.marka}, Model: {self.model}")

# Kullanım
araba1 = Araba("Toyota", "Corolla")
araba1.bilgileri_yazdir()

# Yorum
# Araba sınıfı bir şablon oluşturuyor, __init__ metodu constructor 
# olarak nesne oluşturulurken marka ve model bilgilerini alıp sakılıyor, 
# bilgileri_yazdir metodu ise bu bilgileri ekrana yazdırıyor. Kullanım 
# kısmında Toyota Corolla özelliklerine sahip araba1 nesnesi oluşturuluyor 
# ve metodu çağrılınca "Marka: Toyota, Model: Corolla" çıktısı alınıyor