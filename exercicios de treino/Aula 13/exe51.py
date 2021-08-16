p = int(input('Primeiro termo: '))
razao = int(input('RAZÃO:'))
decimo = p + (10 -1) * razao
for c in range(p, decimo + razao, razao):
     print('{}'.format(c), end=' ')