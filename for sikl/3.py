a , b = map(int,input().split())

if a < b:
    a+=1
    for i in range(a, b):
        print(i)