#35 - dars Xatola bilan ishlash

# son = input("Yoshingizni kiriting?\n>>>")

# try:
#     son = int(son)
#     print(f"Siz {2022-son} yilda tugilgansiz")

# except:
#     print("Siz butun son kiritmadingiz?")



while True:
    son = input("Yoshingizni kiriting?\n>>>")
    if son.isdigit():
        son = int(son)
        break

print(f"Siz {2022-son} yilda tugilgansiz")
