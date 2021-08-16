'''PROGRAMA DEVE MOSTRAR A TABUADA DE VARIOS NUM UM DE CADA VEZ
PARA CADA VALOR QUE O USUARIO QUISER.
SERA INTERROMPIDO QUANDO O NUMERO FOR NEGATIVO'''

while True:
    n = int(input('what tabuada you want see? '))
    print('-'*30)
    if n < 0:
        break
    for cont in range (1,11):
        print(f'{n} x {cont} = {n*cont}')
    print('-'*30)
print('We finish this rigth now!')

