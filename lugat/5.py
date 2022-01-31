dictionary = {'boolean': 'mantiqiy qiymat', 'float': 'o\'nlik son', 'for': 'biror amalni qayta-qayta bajarish sharti', 'if': 'shartlarni tekshirish operatori', 'integer': 'butun son', 'else': 'aks xolda', 'print': 'konsulga chiqarib beradi', 'values': 'lugatdagi qiymatlarni chiqarish', 'keys': 'lugatdagi kalitlarni korish'}
for keys, value in dictionary.items():
    print(f"Kalit: {keys.title()}")
    print(f"Qiymat: {value.title()}\n")