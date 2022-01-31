a, b, c = map(int,input().split())

if c < a and c < b:
    print(c)

elif a < b and a < c:
    print(a)

elif b < a and b < c:
    print(b)

else:
    print("hammasi bir hil")