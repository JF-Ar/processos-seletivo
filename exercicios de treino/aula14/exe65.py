#n = int(input('Insert a number: '))
#resp = str(input('Do you want keep this? [YES/NO] ')).strip().upper()
#c = 0                              (ERRO FOI NÃO ATRIBUIR UM VALOR ANTERIORMENTE PARA O WHILE!!!!!!!!!!)
resp = 'Yy'
media = soma = quantidade = maior = menor = 0
while resp in 'Yy':
    n = int(input('Insert a number: '))
    soma = soma + n
    quantidade += 1
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Do you want keep this? [YES/NO] ')).strip().upper()[0]
media = soma / quantidade    
print('The valor media is {:.2f}'.format(media))
print('The big valor was {} and o menor {}'.format(maior, menor))