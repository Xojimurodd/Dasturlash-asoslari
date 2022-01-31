# 21-dars funksiya vazifa
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()} ning bahosini qoying?\n>>>")
#         baholar[ism] = int(baho)
#     return baholar

# talabalar = ['xojimurod','olim', 'fazlddin', 'mustafo', 'otabek']
# baholar = bahola(talabalar[:])
# print(baholar)
# print(f"Jurnal")
# for bahola in baholar:
#     print(f"Talaba {bahola.title()} ning bahosi")
# print(talabalar)




# def katta_harf(ism):
#     # ism = ism[:]
#     for i in range(len(ism)):
#         ism[i] = ism[i].title()
#     return ism

# ismlar = ['xojimurod', 'fazlddin', 'ota', 'mustafo','anvar']
# katta_harf(ismlar)
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)