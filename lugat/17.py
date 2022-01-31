# #20-qiymat qaytaruvchi funksiya vazifa#

# def mijoz_info(ism, familiya, tyil, tjoy, email = "", tel = None):
#     mijoz = {
#         "ism": ism,
#         "familiya": familiya,
#         "tyil": tyil,
#         "yoshi": 2020 - tyil,
#         "tjoy": tjoy,
#         "email": email,
#         "telefon": tel,
#     }
#     return mijoz  
    

# print(f"Mijoz haqidagi malumotlarni kiriting?")
# mijozlar = []

# while True:
#     ism = input(f"Ismi:".title())
#     familiya = input(f"Familiyasi:".title())
#     tyil = int(input(f"Tug'ilgan yili:"))
#     tjoy = input(f"Tug'ilgan joyi:".title())
#     email = input(f"Email:")
#     telefon = input(f"Telefon raqami:")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     savol = input(f"Davom etasizmi? yes/no")
#     if savol != 'yes':
#         break

# print(f"Mijoz haqida ma'lumot")
# for mijoz in mijozlar:
#     print(
#         f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#         f" {mijoz['yoshi']} yoshda telefoni:{mijoz['telefon']}" 
#         )





# def aylana_radiusi(radius, pi = 3.14):
#     radius = {
#         "radius": radius,
#         "diametr": 2 * radius,
#         "perimetr": 2 * radius * pi,
#         "yuza": pi * radius ** 2,
#     }
#     return aylana_radiusi
# radiuslar = []
# while True:
#     radius = int(input(f"Radiusni kiriting?"))
#     radiuslar.append(aylana_radiusi(diametr,perimetr,yuza))

#     javob = input(f"Yana malumot qoshasizmi? yes/no")

#     if javob != 'yes':
#         break

#     print("Radiuslar")
#     for radius in radiuslar:
#         print(f"{radius['radius']}, {radius['diametr']}")


# def tub_sonlar(min, max):
#     sonlar = []
#     for i in range(min, max+1):
#         tub = True
#         if i == 1:
#             tub = False
#         elif i == 2:
#             tub = True
#         else:
#             for x in range(2, i):
#                 if i % x == 0:
#                     tub = False
    
#         if tub:
#             sonlar.append(i)
#         return sonlar

