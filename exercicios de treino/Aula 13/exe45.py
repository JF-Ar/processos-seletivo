from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
while True:
    print('''SUAS OPÇÕES:
    ---------------------
    [ 0 ] |  PEDRA      |
    [ 1 ] |  PAPEL      |
    [ 2 ] | TESOURA     |
    [999] | SAIR        |
    ---------------------''')
    jogador = int(input('Qual a sua jogada? '))
    if jogador == 999:
            break
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔO!!')
    sleep(0.2)
    print('-='*12)
    print('Você JOGOU {}'.format(itens[jogador]))
    print('O computador JOGOU {}'.format(itens[computador]))
    print('-='*12)
    if computador == 0: #PC PEDRA
        if jogador == 0:
            print('EMPATOU')
        elif jogador == 1: 
            print('+'*10)
            print('VOCÊ GANHOU! BOA!!')
            print('+'*10)
        elif jogador == 2:
            print('VOCÊ PERDEU KKKKKKK!')
        ###else:
           ### print('*' * 8)
          ####  print('JOGADA INVÁLIDA, AMIGÃO!!')              ###JOGADA INVALIDA NÃO FUNCIONAL
          ###  print('*' * 8)'''
    elif computador == 1: #PC PAPEL
        if jogador == 0:
            print('VOCÊ PERDEU KKKKKKK!')
        elif jogador == 1:
            print('EMPATOU')
        elif jogador == 2:
            print('+'*10)
            print('VOCÊ GANHOU! BOA!')
            print('+'*10)
        ###else:
          ###  print('*' * 8)
          ###  print('JOGADA INVÁLIDA, AMIGÃO!!')              ## JOGADA INVALIDA NÃO FUNCIONAL
          ###  print('*' * 8)'''
    elif computador == 2: #PC TESOURA
        if jogador == 0:
            print('+'*10)
            print('VOCÊ GANHOU! BOA!')
            print('+'*10)
        elif jogador == 1:
            print('VOCÊ PERDEU KKKKKKK!')
        elif jogador == 2:
            print('EMPATOU')
        ####else:
         ###   print('*' * 8)
          ###  print('JOGADA INVÁLIDA, AMIGÃO!!')             ##  JOGADA INVALIDA NÃO FUNCIONAL
          ###  print('*' * 8)'''
print('Obrigado por jogar!')