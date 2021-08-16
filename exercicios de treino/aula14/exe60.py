'''from math import factorial
n = int(input('Digite um numero para calcularmos o seu fatorial: '))
fat = factorial(n)
print('{}! é igual a {}'.format(n, fat))'''

'''from math import factorial'''


n = int(input( 'Digite um numero para calcularmos o seu fatorial: '))
c = n
fatorial = 1
print('Calculando {}! ->'.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end='')
    print('x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print('{}'.format(fatorial))