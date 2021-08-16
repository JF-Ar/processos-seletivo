from random import randint
comp = randint(0, 10)
print('Fala maluco, eu pensei num nuemro entre 0 - 10.')
print('Duvido tu acertar. kkkkkkk ')
certo = False
cont = 0
while not certo:
    jogador = int(input('Qual você acha que foi? '))
    cont += 1
    if jogador == comp:
        certo = True
    else:
        if jogador < comp:
            print('Um pouco mais, amigão. Vai de novo: ')
        elif jogador > comp:
            print('Menos né! Vai mais uma: ')
print('Acertou miseravel! Com  {} tentativas.'.format(cont))
