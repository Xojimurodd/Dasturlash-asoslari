son = int(input("Sonni kiriting:"))
birlar = son%100%10
onlar = son%100//10
yuzlar = son//100
print(birlar == yuzlar)