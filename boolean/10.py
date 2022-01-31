x1, y1 = map(int,input().split())
print((x1 %2 == 0 or y1 %2 == 1) and (x1 %2 == 1 or y1 %2 == 0))