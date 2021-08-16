from os import pipe
from time import sleep

nu1 = int(input('Primeiro valor: '))
nu2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('''
    | [ 1 ] Somar          |
    | [ 2 ] Multiplicar    |
    | [ 3 ] Maior          |
    | [ 4 ] Novos Numeros  |
    | [ 5 ] Sair           |''')
    opc = int(input('Escolha uma opção: '))
    if opc == 1:
        soma = nu1 + nu2
        print('A SOMA entre {} e {} é {}'.format(nu1, nu2, soma))
    elif opc == 2:
        mult = nu1 * nu2
        print('O resultado de {} x {} é {}'.format(nu1, nu2, mult))
    elif opc == 3:
        if nu1 > nu2:
            maior = nu1
        else:
            maior = nu2
        print('O maior numero entre {} e {} é o {}'.format(nu1,nu2,maior))
    elif opc == 4:
        print('Beleza, espertinho...')
        nu1 = int(input('Primeiro valor: '))
        nu2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Acabou então...')
    else:
        print('Opção inválida. Tente de novo.')
    print('-='*8)
    sleep(1)
