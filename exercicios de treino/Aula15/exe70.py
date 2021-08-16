'''leia o nome e o preço dos produtos; pergunt se quer continuar
mostre: a) total gasto na compra b) quantos produtos +1000 c) nome do mais barato'''
print('^~~^'*4)
print(' SUA COMPRA AQUI ')
print('^~~^'*4)
total = mil = cont = menor = 0
maisbarato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Valor do produto: R$'))
    cont +=1
    total = total + preço
    if preço >= 1000:
        mil = mil + 1
    if cont == 1 or preço < menor:                 #ABREVIADO POIS SE REPETE NO ELSE (MENOR = PREÇO
        menor = preço                                                 # MAIS BARATO = PRODUTO)
        maisbarato = produto
    '''else: 
        if preço < menor:
            menor = preço
            maisbarato = produto'''
   
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
print(f'O total da sua compra foi: R${total:.2f}')
print(f'Você comproou {mil} produto por mais de R$1000.00')
print(f'O produto mais barato foi {maisbarato}')