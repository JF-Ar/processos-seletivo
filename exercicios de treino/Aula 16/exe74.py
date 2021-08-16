from random import randint


num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Valores sorteados: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(num)} ')   ### funcionalidade do proprio python para show o maior!!!1
print(f'O menor valor sorteado foi {min(num)}')      ### funcionalidade do proprio python para show o menor!!1