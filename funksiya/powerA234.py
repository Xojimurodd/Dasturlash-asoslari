def daraja(n):
    return lambda x:x**n

kvadrat = daraja(2)
kub = daraja(3)
tortinchi = daraja(4)
print(f"-ning kvadrati {kvadrat()} ga,"
      f"kubi {kub()} ga,"
      f"tortinchi darajasi {tortinchi()} ga teng")