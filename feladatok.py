# http://info.nytta.hu/temak/prog/Programozasi_tetelek.pdf

# sorozatszámítás, 1. feladat:
# tesztek: 3 => 6; 4 => 10; 6 => 21;
n = int(input('írd be az N értékét: '))

sum = 0
for n in range(1, n + 1):
    sum += n
print(f"számok összege {n}-ig: {sum}")

# sorozatszámítás, 2. feladat:
# tesztek: 3 => 6; 4 => 24; 5 => 120;
mult = 1
for n in range(1, n + 1):
    mult *= n
print(f"számok szorzata {n}-ig: {mult}")

# eldöntés, 6. feladat:
# tesztek: "alma" -> nem; "alma a fa alatt" -> igen
szoveg = input('írj be egy szöveget: ')
i = 0
while i < len(szoveg) and szoveg[i] != ' ':
    i += 1
if i < len(szoveg): print('több szóból áll')
else: print('a szöveg csak egy szó')