import random as rnd
t = []
for n in range(100):
    t.append(rnd.randint(10, 99))
for i in range(len(t)):
    if i % 20 == 0: print()
    print(t[i], end= ' ')

# sorozatszámítás - összegzés:
sum = 0
for n in t:
    sum += n
print(f'\nOP: számok összege: {sum}')

# sorozatszámítás - szorzat:
k = [1, 2, 3, 4, 5]
mult = 1
for n in k: mult *= n
print(f'OP: k[] elemeinek szorzata: {mult}')

# sorozatszámítás - konkatenáció:
v = ['meg', 'szent', 'ség', 'telenít']
szoveg = ''
for szo in v: szoveg += szo
print(f'OP: v[] szavai összefűzve: {szoveg}')

# NEM TÉTEL, de ebből következik:
# számtani átlag:
print(f'OP: t[] átlaga: {sum / len(t)}')