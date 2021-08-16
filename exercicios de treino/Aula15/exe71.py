'''Pergunte ao user qual o valor a ser sacado;
o programa deve informar quantas cedulas de cada valor serão entregues.
CONSIDERAR CAIXA COM 50;20;10;1 (NOTAS)'''
from time import sleep


print('=-'*20)
print('{:^20}'.format('Bem-vindo ao caixa JF-Ar'))
print('-='*20)
saque = float(input('Qual será o valor do saque? R$'))

total = saque
ced = 50
totalced = 0
#print('''Temos notas de: 
#|R$50.00 | 
#|R$20.00 |
#|R$10.00 |
#|R$1.00  |''')'''
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Executando um total de {totalced} cédulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
             ced = 1
        totalced = 0
        if total == 0:
            break
        
    #saque = float(input('Qual valor do saque? R$')
    #if saque 