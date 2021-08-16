class CaixaEletronico():

    def apresentacao():
        print('{:=^20}'.format(' LOJAS JF-Ar '))
        

    def calcular_pagamento():
        preco = float(input('Qual o valor da compra: R$'))
        print('''\n FORMA DE PAGAMENTO
        [ 1 ] À vista dinheiro/cheque (desconto)
        [ 2 ] À vista cartã (1x)
        [ 3 ] 2x no cartão
        [ 4 ] 3x ou mias no cartão (Juros)''')
        opção = int(input('Qual é a opção? '))
        if opção == 1:
            total = preco - (preco * 10 / 100)
            print(f'Sua comprar tera será de {total}, com o desconto aplicado.')
        elif opção == 2:
            total = preco - (preco * 10 / 100)
            print('Sua compra será parcelada em 1x de R${:.2}, com desconto aplicado'.format(total))
        elif opção == 3:
            total = preco
            parcela = total / 2
            print('Sua compra será parcelada em 2x de R${:.2}'.format(parcela))
        elif opção == 4:
            total = preco + (preco * 20 / 100)
            op4 = int(input('Vai dividir de quantas vezes? '))
            parcela = total / op4
            print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(op4, parcela))
        else:
            total = 0
            print('Opção invalidada de pagamento, tente novamente com um opção válida')
        print('Sua compra de R${:.2f} vai custar R${:.2f} !'.format(preco, total))


    apresentacao()
    calcular_pagamento()
CaixaEletronico()
