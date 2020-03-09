lista = []
for y in range (10):
    num= (int(input('Entre com valor:  ')))
    lista.append(num)
print('Maior número', max(lista))
print('Menor número', min(lista))
media= sum(lista)/10
print('Média',media)
print('Some', sum(lista))
for y in range(10):
    if y < media:
        print('Os valores menores que média : ',y)

        # for y in lista:
        #     if y < media //percorrendo pelo indice
