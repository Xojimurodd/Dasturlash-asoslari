a, b, c = map(int,input().split())

if b < a and c < b:
        print(b)

elif a < b and c < a:
        print(a)

elif c < a and c < b:
        print(c)

else:
    print("hammasi bir xil")