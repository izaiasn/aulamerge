n = int(input('Digite um valor para ver sua tabuada: '))
print('-' *12)
for c in range (1,11):
    print('{} X {:2} = {}'.format(n, c, n*c))
