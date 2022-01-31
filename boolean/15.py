x1, y1, z1 = map(int,input().split())
print((x1 >= 0 and y1 >= 0 and z1 < 0) or (x1 < 0 and y1 >= 0 and z1 >= 0) or (x1 >= 0 and y1 < 0 and z1 >=0))