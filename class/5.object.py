# #30-dars Vorislik va Polimorfizm vazifasi


class Shaxs:
    def __init__(self,ism,familiya,pasport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.pasport = pasport
        self.tyil = tyil

    def get_info(self):
        info = f"{self.familiya} {self.ism}",
        info+=f"Passport:{self.pasport}, {self.tyil}-da tugilgan"
        return info

    def get_age(self,yil):
        return yil-self.tyil

inson = Shaxs("Xojimurod","Xomidov","FB2004123",2004)
inson.get_info()


class Talaba:
    def __init__(self,ism,familiya,tyil,fanlar):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.fanlar = []


class Fan(Talaba):
    def __init__(self, ism, familiya, tyil, fanlar,matematika,fizika,kimyo,adabiyot):
        super().__init__(ism, familiya, tyil, fanlar)
        self.matematika = matematika
        self.fizika = fizika
        self.kimyo = kimyo
        self.adabiyot = adabiyot