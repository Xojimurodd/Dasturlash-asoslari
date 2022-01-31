#28-dars object orented dasturi vazifasi


class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    def get_name(self):
        print(self.ism)


talaba1 = Talaba("Xojimurod","Xomidov",2004)
talaba2 = Talaba("Mustafo","Shokirov",2004)
talaba3 = Talaba("Fazlddin","Dehqonov",2004)
talaba3.get_name()