soma = 0
media = 0
maior_idade = 0
maisvelho = ' '
total20 = 0
for p in range(1, 5):
    print('--- {}° PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sex = str(input('Sexo [M/F] ')).strip()
    soma +=idade
    if p == 1 and sex in 'Mm':
        maior_idade = idade
        maisvelho = nome
    if sex in 'Mm' and idade > maior_idade:
        maior_idade = idade
        maisvelho = nome 
    if sex in 'Ff' and idade < 20:
        total20 += 1
media = soma / 4
print('A idade media do grupo é de {}'.format(media))
print('O homem mais velho é {} que tem {} anos'.format(maisvelho, maior_idade))
print('Ao todo, nessa lista, temos {} mulheres com menos de 20 anos'.format(total20))