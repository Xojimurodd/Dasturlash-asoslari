#18- dars While royxatlar bilan ishlash vazifa

ismlar = []
n = 1
while True:
    savol = f"{n}- do'stingizni kiritng"
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input(f"Yana ism qo'shasizmi? (ha/yoq) ")
    n+=1
    if takrorlash != 'ha':
        break

print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())





# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Ismingizni kiriting?\n>>>")
#     yosh = input(f"{ism.title()}ning yoshini kiriting?\n>>>")
#     dostlar[ism] = int(yosh)

#     javob = input(f"Yana ma'lumot qo'shasizmi? (ha/yoq) ")

#     if javob != 'ha':
#         ishora = False

# print("Do'stlaringiz ro'yxati:")
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()}ning yoshi {yosh}da")



# ismlar = ['Fazlddin', 'Xoji', 'Xoji', 'Xoji','Fazlddin','Xoji']
# while 'Xoji' in ismlar:
#     ismlar.remove('Xoji')
#     print(ismlar)



# oquvchilar = ['Xojimurod','fazlddin', 'lazizbe','mustafo','otabek','sevinchbe','abdulvosid']
# baholangan_oquvchilar = {}
# while oquvchilar:
#     oquvchi = oquvchilar.pop()
#     baho = input(f"{oquvchi.title()}ning bahosini kiriting")
#     print(f"{oquvchi.title()} baholandi")
#     baholangan_oquvchilar[oquvchi] = int(baho)



# savat = []
# while True:
#     mahsulot = input("Savatga mahsulot qo'shing:")
#     savat.append(mahsulot)
#     javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
#     if javob != "ha":
#         break
# print(savat)




# e_bozor = {}

# while True:
#     bozorlik = input("Bozorlik uchun maxsulot qoshin?\n>>>")
#     narx = input(f"{bozorlik.title()}ning narxini kiriting?\n>>>")
#     e_bozor[bozorlik] = int(narx)

#     javob = input("Yana ma'lumot qo'shasizmi? ha/yo'q\n>>>")

#     if javob != "ha":
#         break

# print("Bozoringiz royhati")
# for bozorlik, narx in e_bozor.items():
#     print(f"{bozorlik}ning narxi {narx} so'm")

# buyurtmalar = ["olma", "anjir", "uzum", "qovun"]
# mahsulotlar = {"olma": 20000, "shaftoli": 25000, "tarvuz": 18000, "uzum": 22000}
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narx = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narx} so'm")

#     else:
#         print(f"Bizda {buyurtma} yo'q")
