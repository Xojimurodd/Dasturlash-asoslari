tezlik = 15
oqim_tezligi = 4
time_for_go = 2
time_for_come = 3
way_for_go = (tezlik + oqim_tezligi) * time_for_go
way_for_come = (tezlik - oqim_tezligi) * time_for_come
full_way = way_for_go + way_for_come
print(full_way)