#29-dars object orented dasturi vazifasi


class Avto:
    def __init__(self,model,rang,karobka,narx):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narx = narx
        self.kilometr = 0
        
    def get_info(self):
        return f"Modeli: {self.model}, Rangi: {self.rang}, Karobka: {self.karobka}, Narx: {self.narx}, Kilometr: {self.kilometr}"

    def set_km(self,yangi_kilometr):
        self.kilometr = yangi_kilometr

    def update_km(self):
        self.kilometr+= 'km'

avto = Avto("GM","qizil","avtomat",60000) 
print(avto.get_info())