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

print("Davlatlar:")
for davlat in sorted(davlatlar):
     print(davlat.upper())

print("\nDavlatlarning poytaxtlari:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())

