a, b, c = map(int,input().split())
musbat = 0
manfiy = 0

if a > 0:
    musbat +=1

    if b > 0:
        musbat +=1

        if c > 0:
            musbat +=1
            print(musbat)

        elif c < 0:
            manfiy +=1
            print(manfiy)

    elif b < 0:
        manfiy +=1
        print(manfiy)

        if c > 0:
            musbat +=1
            print(musbat)

        elif c < 0:
            manfiy +=1
            print(manfiy)

elif a < 0:
    manfiy +=1
    print(manfiy)

    
    if b > 0:
        musbat +=1

        if c > 0:
            musbat +=1
            print(musbat)

        elif c < 0:
            manfiy +=1
            print(manfiy)

    elif b < 0:
        manfiy +=1
        print(manfiy)

        if c > 0:
            musbat +=1
            print(musbat)

        elif c < 0:
            manfiy +=1
            print(manfiy)
