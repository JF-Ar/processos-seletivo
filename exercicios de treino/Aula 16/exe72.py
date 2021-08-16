def num_por_extenso():
    resp = ''
    extenso = ('zero', 'um','dois','três','quatro','cinco'
                'seis','sete','oito','nove','dez','onze','doze',
                'treze','quatorze','quinze','dezesseis','dezessete',
                'dezoito','dezenove','vinte')
    while resp in 'Ss':
        while True:
            num = int(input('Digite um numero entre 0 e 20: '))
            if 0 <= num <= 20:
                break
            print('Ta errado, amigo. ', end='')
        print(f'Você digitou {extenso[num]}.')
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    print('Tão ta joia, amigo.')

num_por_extenso()