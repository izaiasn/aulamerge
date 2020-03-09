n = int(input('Digite um valor: '))
r = int(input('Digite a razão: '))
dec = n + (10 - 1) * r
for c in range (n, dec + r, r ):
    print('{}'.format(c), end='-|')
print('Fim')