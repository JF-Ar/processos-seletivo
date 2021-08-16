'''ENQUANTO [VERDAEITO]              while true:
        SE []                            if []      
            PASSO                            passo  
       SE []                             if []
            PULA                             pula
        SE []                            if []
            PEGA                             pega
        SE {}                            if {}
            PULA                             pula
            INTERROMPA                       break
    PEGA                              pega'''  

    #NESSE CASO, WHILE TEM LAÇO INFINITO, POR ISSO A NECESSIDADE DO "BREAK";

'''cont = 1
while cont <= 10:   #while true -> sempre
    print(cont, end='')
    cont += 1
print('Acabou')'''

'''n = s = 0
while n != 999:
    n = int(input('Digite um numero'))
    s += n
s -= 999                                    <-  #GAMBIARRA!!! o jeito de arrumar isso segue abaixo
print('A soma vale {}'.format(s))'''


n = s = 0
while True:                           #LAÇO INFINITO 
    n = int(input('Digite um numero: '))
    if n == 999:                              #GAMBIARRA RESOLVIDA with break
        break
    s += n
#print('A soma é {}'.format(s))
print(f'A soma é {s}')                     #FORMA MAIS NOVA DO PYTHON -> F STR
