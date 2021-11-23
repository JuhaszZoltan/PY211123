# kiválasztás, 4. feladat:
# kifejezetten ROSSZ megoldás #
# tesztek: "augusztus" -> nyar; "aprilis" -> tavasz
tavasz = ['tavasz', 'mar', 'apr', 'maj']
nyar = ['nyár', 'jun', 'jul', 'aug']
osz = ['ősz', 'szept', 'okt', 'nov']
tel = ['tél', 'dec', 'jan', 'feb']
ev = [tavasz, nyar, osz, tel]

honap = input('írd be egy hónap nevét: ')

for evszak in ev:
    if honap in evszak: print(evszak[0])