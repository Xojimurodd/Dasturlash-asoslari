a , b = map(int,input().split())
sum = 0

if a < b:
    for i in range(a, b):
        sum+=i
        print(sum)