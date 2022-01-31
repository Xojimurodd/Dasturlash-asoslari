#31-dars  INKAPSULYATSIA, KLASSNING XUSUSIYAT VA METODLARI 
                                        #VAZIFA

# from uuid import uuid4
# id = uuid4()
# print(f"Sizning idingiz: {id}\nIdingizni chundizmz?")
# savol = input(">>>")
# if savol == 'ha':
#     print("Sog boling")
# else:
#     print("Men ham tushunmaganman boshida.Sog boling")


from uuid import uuid4

class Avto:
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto+=1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    
    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

avto = Avto("GM","Malibu","qizil",2004,100000,10000)
print(avto.get_km())
print(avto.get_id())