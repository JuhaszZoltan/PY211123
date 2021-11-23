t = [7, 10, 3, 13, 5, 9, 2, 31, 11, 26]

# szélsőérték-hely meghatározás: maximum
maxi = 0
for i in range(1, len(t)):
    if t[i] > t[maxi]:
        maxi = i
print(f'az adatszerkezet legnagyobb eleme {t[maxi]}, ez a lista {maxi}. indexű eleme')

# szélsőérték-hely meghatározás: minimum
mini = 0
for i in range(1, len(t)):
    if t[i] < t[mini]:
        mini = i
print(f'az adatszerkezet  legkisebb eleme {t[mini]}, ez a lista {mini}. indexű eleme')
