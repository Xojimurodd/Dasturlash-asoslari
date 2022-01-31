davlatlar = {
    'uzbekiston': 'toshkent',
    'rossiya': 'moskva',
    'angliya': 'london',
    'germaniya': 'berlin',
    'fransiya': 'parij',
    'ispaniya': 'madrid',
    'aqsh':'washington',
    'turkiya': 'istanbul',
    'koreya': 'seul',
    'xitoy': "ganko'ng",
    }
country = input("Qaysi davlatni poytaxtini bilishni istaysiz?:").lower()
capital = davlatlar.get(country)

if davlatlar == None:
    print("Kechirasiz, bizda bu haqida malumot yoq")
    

else:
    print(f"{country.title()}ning poytaxti {capital.title()} shahri")
    

     
