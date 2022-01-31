#33-dars Fayllar bilan ishlash


# import pickle


# talaba1 = ['Xojimurod','Xomidov',2004,'Zarkent','1-kurs']
# with open('talaba1','wb') as file:
#     pickle.dump(talaba1,file)



# with open('pi_million_digits.txt') as file:
#     pi = file.read()
# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = pi.replace('','')
# bdate = ""
# print(bdate in pi)

# with open('pi_million_digits.txt') as file:
#     pi = file.read()

# pi = pi.replace('\n','')
# pi = float(pi)
# print(pi)



# import pickle

# filename = 'new_file_pi'
# pi = 'pi_million_digits_txt'

# with open('filename','wb') as file:
#     file.write(pi)






# book = 'new_file.txt'
# while True:
#     ism = input(f"Ismingizni kiriting?\n>>>")
#     familiya = input(f"Familiyangizni kiriting?\n>>>")
#     tyil = int(input(f"Tugilgan yilingizni kiriting? (to'xtash uchun Enter bosing):\n>>>"))
#     if not tyil:
#         break
                      
#     with open("book", 'a') as file:
#         file.write(ism+'\n')
#         file.write(familiya+'\n')
#         file.write(str(tyil))

# while True:
#     book = input("Yaxshi ko'rgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
#     if not book:
#         break
#     with open("book", "a") as file:
#         file.write(book + "\n")