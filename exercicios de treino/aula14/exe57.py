sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Vamo tentar de novo. Qual o seu sexo [M/F] '))
print('Obrigado por responder.')