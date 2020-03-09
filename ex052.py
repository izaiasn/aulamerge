n = int(input('Digite um valor par saber se ele é um número primo: '))
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
    else:
        print('\033[33m', end='')
    print ('{}'.format(c), end='')
