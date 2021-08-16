print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
userterm = 0
more = 10
while more !=0: 
    userterm = userterm + more
    while cont <=userterm:
        print('{} -> '.format(termo), end = '')
        termo += razão
        cont += 1
    print('PAUSE')
    more = int(input('How mach numbers do you want see? '))
print('Your PA are finished with {} terms showed !')
