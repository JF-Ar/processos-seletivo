'''for c in range(1, 10): #enquanto o contador não chegar a 10
    print(c)
print('fim')'''

'''c = 1                ##o contador já começar com 1
while c < 10:       #enquanto o contador for menor que 10
    print (c)
    c = c + 1       ##Quando ele voltar, é importante que se some 1 no C
print ('Fim')'''

def par_impar():
    n = 1 
    par = impar = 0
    while n != 0 :
        n = int(input('Digite um valor: ')) 
        if n % 2 == 0:
            par += 1 
        else:
            impar +=1
    print('Você digitou {} numeros pares e {} numeros impares.'.format(par, impar))

par_impar()