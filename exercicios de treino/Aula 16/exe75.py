numeros = (int(input('Digite um numero: ')), int(input('Digite mais um numero: ')),
            int(input('Digite outro numero: ')), int(input('Digite o ultimo numero: ')))
print(f'Você digitou os valores {numeros}')
print(f'The number nine apareceu {numeros.count(9)}')
if 3 in numeros:
    print(f'The number três apareceu pela primeira vez nº {numeros.index(3)+1}°')   
print(f'The number par digitado foi: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n} ', end='')