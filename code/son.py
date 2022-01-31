#36-dars Funksiyani tekshirish vazifa

def kotta_son(x,y,z):
    
# x,y,z = map(int,input("3 ta son kiriting").split())
    if x > y > z:
        print(f"Eng kottasi: {x} ")
    elif x < y > z:
        print(f"Eng kottasi: {y} ")

    elif x < y < z:
        print(f"Eng kottasi: {z} ")
    else:
        print(f"Siz kiritgan sonlar hammasi teng")

print(kotta_son(3,4,5))