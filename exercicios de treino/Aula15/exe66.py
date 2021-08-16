'''LEIA VARIOS NUMEROS INTEIROS. O PROGRAMA SÓ PARA QUANDO O USER DIGITAR 999; 
NO FIM, MOSTRE QUANTOS NUMEROS FORAM DIGITADOS E A SOMA ENTRE ELES (DESCONSIDERANDO A FLAG)'''

s = n = cont = 0
while True:
    n = int(input('Digite um numero [999 STOP THE COUNT]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foram digitados {cont} numeros e a soma entre eles é {s}')

