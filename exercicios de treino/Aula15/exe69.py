'''LEIA A IDADE, SEXO DE VARIAS PESSOAS. CADA PESSOA PERGNT SE QUER CONT OU NÃO;
NO FIM MOSTRE: A) QUANTAS PESSOAS TEM +18 B) QUANTOS HOMENS C) QUANTAS MULHERES TEM MENOS DE 20'''

idade = 0
cont = 0
resp = ''
maior = 0
contM = 0
while resp in 'Ss':
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        cont = cont + 1
    if sexo in 'Mm':
        contM +=1
    contF = 0
    if sexo in 'Ff' and idade < 20:
        contF +=1
    print('='*20)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('='*20)
    if resp in 'Nn':
        break
    #cont +=1  cont no lugar errado
print(f'No grupo tem {cont} maiores de idade.')
print(f'No grupo temos {contM} do sexo MASCULINO')
print(f'No grupo temos {contF} do sexo FEMININO com menos de 20 anos')
#print('testando')
'''    cont 
    if idade >= 18: mesmo erro de cima do cont'''