lista = [90, 20, 30, 33, 34, 35, 70, 89, 49, 22, 11, 22, 33, 44, 11, 99, 22]
lista_par = []
lista_imp = []
for item in lista:
    if item % 2 == 0:
        lista_par.append(item)
    if item % 2 == 1:
        lista_imp.append(item)
print(' lista par', lista_par)
print('lista impar', lista_imp)
