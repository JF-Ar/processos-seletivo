Listagem = ('Lápis', 1.23,
            'Borracha',0.50,
            'Caderno', 14.00,
            'Estojo', 20.00,
            'Caneta', 2.20,
            'Bolsa', 35.99,
            'Post-it', 10.00,
            'Agenda', 7.50  )
print('~~'*19)
print(f'{" OPÇÕES DE PREÇOS: ":^35}')   ##DUAS ASPAS PARA NÃO CONFUNDIR NA FORMATAÇÃO
print('~~'*19)
##print(Listagem)       ##Forma mais estranha
'''for item in Listagem:
    print(item)            ##Ainda não é o ideal, já que os itens são mostrados, mas não
                                          de maneira tabular'''
for item in range(0, len(Listagem)):
    if item % 2 == 0:                       ##todos os itens estão na posição PAR
        print(f'{Listagem[item]:.<30}', end='')          ### ':' alinhando '<' à esquerda '30'  trinta caracters
    else:                                   ###preços estão na posição IMPAR
        print(f'R${Listagem[item]:>6.2f}')          
                                                
print('~~'*19)
