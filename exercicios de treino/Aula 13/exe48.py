soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont +1
        s = s + c
print(f'Você tem {cont} valores ímpares e a soma entre eles é {soma}')

