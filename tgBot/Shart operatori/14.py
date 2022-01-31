a, b, c = map(int,input().split())

if a > b:
    if b > c:
        print(c, a)

elif a < b:
    if a > c:
        print(c, b)

elif a > c:
    if c > b:
        print(b, a)