n = int(input())
sum = 1
if n > 0:
    for i in range(11, n):
        i = i/10
        sum*=i
        print(sum)