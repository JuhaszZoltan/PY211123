import random as rnd
t = []
for n in range(100):
    t.append(rnd.randint(10, 99))
for i in range(len(t)):
    if i % 10 == 0: print()
    print(t[i], end= ' ')

# eldöntés - T = 'van-e benne 17el osztható elem'
i = 0
while i < len(t) and t[i] % 17 != 0:
    i += 1
if i < len(t): print(f'\na tulajdonság teljesül')
else: print('\na tulajdonság NEM teljesül')

# python specifikus implementáció (v2)
# [mivel bármilyen numerikus számítás eredménye ha 0, akkor az ekvivalens a logikai False értékkel]
i = 0 
while i < len(t) and t[i] % 17:
    i += 1
if i < len(t): print(f'a tulajdonság teljesül')
else: print('a tulajdonság NEM teljesül')

# ha nem kell 'zárt' algoritmus, akkor a következőek is elfogadhatóka:
# [pythonban nem része a CCnek a zárt alg.]
# [pythonban a ciklusok 'ELSE ága'm akkor fut le, ha a ciklos alatt sosem volt break]
for n in t:
    if n % 17 == 0:
        print('a tulajdonság teljesül')
        break
else: print('a tulajdonság NEM teljesül')
# vagy
i = 0
while i < len(t):
    if t[i] % 17 == 0:
        print('a tulajdonság teljesül')
        break
    i += 1
else: print('a tulajdonság NEM teljesül')

# a tulajdonság természetesen nem csak oszthatóság lehet, hanem bármi
# minden más esetben az összetett feltétel második részébe kell behelyettesíteni a tulajdonság negátját

szavak = ['krumpli', 'pék', 'ló', 'kecske', 'kisegítő iskola']

i = 0
while i < len(szavak) and szavak[i] != 'pingvin':
    i += 1
if i < len(szavak): print('ott van a "pingvin" a szavak között')
else:  print('nincs ott a pinkvin a szavak között')