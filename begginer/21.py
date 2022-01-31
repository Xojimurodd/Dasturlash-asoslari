import math
num_x1 = 4
num_x2 = 5
num_x3 = 7
num_y1 = 6
num_y2 = 9
num_y3 = 13
side_a = math.sqrt((num_x2-num_x1)**2+(num_y2-num_y1)**2)
side_b = math.sqrt((num_x3-num_x2)**2+(num_y3-num_y2)**2)
side_c = math.sqrt((num_x3-num_x1)**2+(num_y3-num_y1)**2)
perimetr = (side_a+side_b+side_c)/2
yuza = math.sqrt(perimetr*(perimetr-side_a)*(perimetr-side_b)*(perimetr-side_c))
print(f"perimetr: {perimetr}\nyuza: {yuza}")