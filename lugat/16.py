# # 19-dars Funkisiya vazifa
# def yosh_hisobla(ism, tugil_yil):
#     """Tugilgan yilini hisoblaydigon programma"""
#     print(f"{ism.title()} {2022-tugil_yil} yoshdasiz")

# yosh_hisobla('Fazlddin',2004 )
# yosh_hisobla('nodirbek', 2006)


# def kvadrat_hisob(son):
#     """kvadrat hisoblash"""
#     print(f"{son} ning kvadrati {son**2}\n{son} ning kubi {son**3}")

# kvadrat_hisob(4)



# def juft_son(son):
#     """Juft yoki toqligini aniqlovchi programma"""
#     if son > 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")

# juft_son(4)




# def ikkita_son(son1, son2):
#     """foydalanuvchidan son qabul qilib teng yoki teng masligini aniqlovchi dastur"""
#     if son1 > son2:
#         print(f"{son1} kotta {son2} dan")

#     elif son2 > son1:
#         print(f"{son2} soni {son1} dan kotta")    

#     else:
#         print(f"{son1} = {son2}")

# ikkita_son(5, 4)


# def ikkita_son(x, y):
#     """x**y ni konsolga chiqaruvchi funksiya."""
#     print(f"{x**y} darajasi")

# ikkita_son(4, 5)



# def ikkita_son(y, standart_q = 2):
#     """x**y ni konsolga chiqaruvchi funksiya."""
#     print(f"{y**standart_q} ning darajasi")

# ikkita_son(3)



# def bolinish_alomatlari( son ):
#     for n in range(2, 11):
#         if not son % n:
#             print(f"{son} {n} ga qoldiqsiz bolinadi")

# bolinish_alomatlari(4)