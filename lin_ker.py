# lineáris keresés
# valójában az eldöntés és a kiválasztás kombinációja:

t = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

i = 0
while i < len(t) and t[i] != pow(2, 6):
    i += 1

if i < len(t):
    print("van találat")
    print(f"a {pow(2, 6)} (2^6) benne van a listában")
    print(f'a lista {i}. indexű eleme ({t[i]})')
else:
    print('nincs találat')
    print('a keresett szám NINCS benne az adatszerkezetbe')

# ----------------------

i = 0
while i < len(t) and t[i] != pow(2, 30):
    i += 1

if i < len(t):
    print("van találat")
    print(f"a {pow(2, 30)} (2^30) benne van a listában")
    print(f'a lista {i}. indexű eleme ({t[i]})')
else:
    print('nincs találat')
    print('a keresett szám NINCS benne az adatszerkezetbe')

# ---------------------
# linker break-el (csak python):

i = 0
while i < len(t):
    if t[i] == pow(2, 6):
        print(f'van találat, a {pow(2, 6)} a lista {i}. indexű eleme')
        break
else: print(f'nincs találat, a {pow(2, 6)} nincs benne a listában')