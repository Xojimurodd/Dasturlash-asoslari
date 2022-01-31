a, b = map(int,input().split())

if a < b:
    b+=1
    for i in range(a, b):
        print(i)

else:
    print("Siz kiritgan a son b dan katta ")