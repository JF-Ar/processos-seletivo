print('-'*22)
print('SEQUENCIA FIBONACCI')
print('-'*22)

n = int(input('How many terms do you want see? '))
term1 = 0
term2 = 1
print('^^'*16)
print('{} -> {}'.format(term1, term2), end='')
cont = 3
while cont <= n:
    term3 = term1 + term2
    cont += 1
    print(' -> {}'.format(term3), end='')
    term1 = term2
    term2 = term3
print(' END!!')
print('^^'* 16)