import random



def sontop(x = 100):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    taxminlar = 0

    while True:
        taxminlar+=1
        tahmin = int(input(">>>"))

        if tasodifiy_son > tahmin:
            print(f"Xato, men oylagan son bundan kattaroq.Yana harakat qiling:")

        elif tasodifiy_son < tahmin:
            print(f"Xato, men oylagan son bundan kichikroq.Yana harakat qiling:")

        else:
            break

    print(f"Tabriklaymiz.Siz men oylagan sonni {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar


def sontop_pc(x=100):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing.Men topaman")

    quyi = 1
    yuqori = x
    taxminlar = 0

    while True:
        taxminlar+=1

        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)

        else: 
            taxmin = quyi
        javob = input(
            f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
            f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()
        )

        if javob == "-":
            yuqori = taxmin-1

        elif javob == "+":
            quyi = taxmin+1

        else:
            break

    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar


def play(x=100):
    yana = True

    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)

        if taxminlar_user < taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")

        
        elif taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")

        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))


play()