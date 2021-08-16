def tabuada():
    num = int(input(('Digite um numero para ver a sua tabuada: ')))
    for c in range(1, 11):
        print(f'| {num} x {c} = {num * c}')
tabuada()