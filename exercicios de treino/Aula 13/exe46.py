from time import sleep

def contagem_regressiva():
    print('CONTAGEM REGRESSIVA PARA O LANÇAMENTO DO FOGUETE, VAI COMEÇAR:')
    for c in range(10, -1, -1):
        sleep(1)
        print(c)
    print('CLAP CLAP CLAP')

    
contagem_regressiva()