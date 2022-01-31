a, b = map(int,input().split())
sum = a

if a > b:
   a=b
   b=sum 
   print(a, b)

else:
    print(a, b)