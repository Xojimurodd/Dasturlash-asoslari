a , b = map(int,input().split())
sum = 1

if a < b:
    for i in range(a, b):
        sum*=i
        print(sum)

else:
    print("Siz kiritgan son b dan kichik")
