num_a1 = 10
num_b1 = 11
num_c1 = 8

num_a2 = 13
num_b2 = 9
num_c2 = 18

D = (num_a1*num_b2-num_a2*num_b1)
x = (num_c1*num_b2-num_c2*num_b1)/D
y = (num_a1*num_c2-num_a2*num_c1)/D
print(f"x: {x}\ny: {y}")