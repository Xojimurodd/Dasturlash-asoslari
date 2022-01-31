a, b, c = map(int,input().split())

counter = 0

if a > 0:
    counter += 1
    if b > 0:
        counter += 1
        if c > 0:
            counter += 1
            print(counter)
        elif c < 0:
            print(counter)
    elif b < 0:
        if c > 0:
            counter += 1
            print(counter)
        elif c < 0:
            print(counter)

elif a < 0:
    if b > 0:
        counter += 1
        if c > 0:
            counter += 1
            print(counter)
        elif c < 0:
            print(counter)
    elif b < 0:
        if c > 0:
            counter += 1
            print(counter)
        elif c < 0:
            print(counter)
