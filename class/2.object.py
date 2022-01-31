#28-dars object orented dasturi vazifasi


class Users:
    def __init__(self,ism,familiya,tyil,email):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.email = email
    def get_info(self):
        print(f"Foydalanuchi: {self.ism}{self.tyil}, ismi: {self.ism.title()} {self.familiya.title()},email: {self.email}")

user = Users("Xojimurod","Xomidov",2004,"xomidovxojimurod007@gmail.com")

user.get_info()