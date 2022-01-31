#16-dars nesting vazifasi

#   m_shaxslar0 = {
#     'ismi': 'Alisher',
#     'familiya': 'Navoiy',
#     't_yil': 1441,
#     't_shahri': 'xirotda',
#     'u.korgan' : 60
# }
# m_shaxslar1 = {
#        'ismi': 'Erkin',
#     'familiya': 'Vohidov',
#     't_yil': 1936,
#     't_shahri': 'farg\'ona',
#     'u.korgan' : 80
# }
# m_shaxslar2 = {
#        'ismi': 'Abdulla',
#     'familiya': 'Qodiriy',
#     't_yil': 1894,
#     't_shahri': 'toshkent',
#     'u.korgan' : 44
# }
# m_shaxslar = m_shaxslar0
# print(f"{m_shaxslar['ismi'].title()} {m_shaxslar['familiya']} {m_shaxslar['t_yil']}-yilda {m_shaxslar['t_shahri'].title()} tavallud topgan. {m_shaxslar['u.korgan']} yil umr korgan.")
# m_shaxslar = m_shaxslar1
# print(f"{m_shaxslar['ismi'].title()} {m_shaxslar['familiya']} {m_shaxslar['t_yil']}-yilda {m_shaxslar['t_shahri'].title()} tavallud topgan. {m_shaxslar['u.korgan']} yil umr korgan.")
# m_shaxslar = m_shaxslar2
# print(f"{m_shaxslar['ismi'].title()} {m_shaxslar['familiya']} {m_shaxslar['t_yil']}-yilda {m_shaxslar['t_shahri'].title()} tavallud topgan. {m_shaxslar['u.korgan']} yil umr korgan.")




# m_shaxslar0 = {
#     'ismi': 'Alisher',
#     'familiya': 'Navoiy',
#     't_yil': 1441,
#     't_shahri': 'xirotda',
#     'u.korgan' : 60,
#     'm_asarlari': ['Xamsa', 'Lison ut-tayr', 'Mahbub al-qulub' ]

# }
# m_shaxslar1 = {
#     'ismi': 'Erkin',
#     'familiya': 'Vohidov',
#     't_yil': 1936,
#     't_shahri': 'farg\'ona',
#     'u.korgan' : 80,
#     'm_asarlari': ['Tong nafasi', 'ozbegim', 'Qiziquvchan matmusa' ]
# }
# m_shaxslar2 = {
#        'ismi': 'Abdulla',
#     'familiya': 'Qodiriy',
#     't_yil': 1894,
#     't_shahri': 'toshkent',
#     'u.korgan' : 44,
#     'm_asarlari': ['otgan kunlar', 'mehrobdan chayon', 'obid ketmon' ]
# }
# m_shaxslar = [m_shaxslar0, m_shaxslar1, m_shaxslar2]

# for m_shaxs in m_shaxslar:
#     ismi = m_shaxs['ismi']
#     m_asarlari = m_shaxs['m_asarlari']
#     print(f"\n{m_shaxs['ismi'].title()} ning mashxur asarlari:")
#     for asar in m_asarlari:
#         print(asar.title())







# kinolar = {
#     'Xurshid': ['Qasoskorlar', 'x_men', 'Tor_3'],
#     'Oyatillo': ['betmen', 'Terminator','Rambo'],
#     'Diyorbek': ['Abdullajon','Bomba', 'tenet']
# }
# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino.title())






# davlatlar = {
#     "ozbekiston": {
#     'poytaxt': 'toshkent', 
#     'maydon': '448978',
#     'aholi': '35_000_000',
#     'pul birligi': 'som'
#     },
#     'Rossiya' : {
#     'poytaxt': 'moskva',
#      'maydon': '17098246',
#      'aholi': '144000000',
#      'pul birligi'  : 'rubl'
#      },
# }

# for davlat, info in davlatlar.items():

#     if davlat.lower() == "ozbekiston":
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(
#     f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}"
#     f"\nHududi: {info['maydon'].title()} Kv.Km"
#     f"\nAholisi: {info['aholi'].title()}"
#     f"\nPul birligi: {info['pul birligi']}"
#     )






davlatlar = {
    "ozbekiston": {
    'poytaxt': 'toshkent', 
    'maydon': '448978',
    'aholi': '35_000_000',
    'pul birligi': 'som'
    },
    'rossiya' : {
    'poytaxt': 'moskva',
     'maydon': '17098246',
     'aholi': '144000000',
     'pul birligi'  : 'rubl'
     },
}
davlat = input("Davlat nomini kiriting?\n>>>").lower()
print(davlat)
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(
    f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}"
    
    f"\nHududi: {info['maydon'].title()} Kv.Km"
    f"\nAholisi: {info['aholi'].title()}"
    f"\nPul birligi: {info['pul birligi']}"
    )
else:
    print("Bizda bu haqida ma'lumot mavjud emas")