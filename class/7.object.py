#32-dars Dunder metodlar  
#                           Vazifa


# matn = 'rgjeriovjtbvjfegbprgnkrghjpbprgrgoibfvjecriodslkcfvgoifkdl'
# print(len(matn))




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
    
    def __rerp__(self):
        return 

inson = Shaxs("Xojimurod","Xomidov","FB2004123",2004)

class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.fanlar = []