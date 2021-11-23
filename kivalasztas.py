t = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

# kiválasztás - akkor használható, ha BIZTOS, hogy van a listámban adott tulajdonságú elem

i = 0
while t[i] != pow(2, 30):
    i += 1
print(f'A kettő hatodik hatványa a lista {i}. indexű eleme ({t[i]})')