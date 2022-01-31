menu = {
    'osh': '1000000 som',
    "non": '20000 som',
    'somsa': '10000 som',
    'shashli': '15000 som',
    'chuchvara': '20000 som',
    'shorva': '14000 som',
    'monti': '5000 som',
    'lagmon': '8000 som',
    'kocha': '12000 som' 
}

print("3 ta taom buyurtma bering?>>>")
buyurtmalar = []

for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:

    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")

    else:
        print(f"Kechirasiz,bizda {buyurtma} yo'q.")
