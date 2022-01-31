#29-dars object orented dasturi vazifasi

class Avtosalon:
    def __init__(self, salon_nomi,manzili,Sotuvdagi_avtomobillar):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.sotuvdagi_avtomobillar = Sotuvdagi_avtomobillar

    def get_info(self):
        print(f"Avtosalon nomi:{self.salon_nomi},Manzili: {self.manzili},Sotuvdagi avtomobillar:{self.sotuvdagi_avtomobillar}")

    def set_avtomobil(self,yangi_avtomobil):
        self.sotuvdagi_avtomobillar = yangi_avtomobil

    def get_avtomobil(self):
        self.sotuvdagi_avtomobillar+= input(f"Mashinalarni kiriting?")

avtosalon = Avtosalon("xojimurod","Zarkent","Malibu")
avtosalon.get_info()
avtosalon.get_avtomobil()
    