import meu_modulo
tupla1=()
tupla2=()

for i in range (3):
    n= int(input('Número'))
    tupla1 += (n,)

for i in range (3):
    n = int(input('Número'))
    tupla2 += (n,)
tupla3 = meu_modulo.intercala(tupla1, tupla2)
print tupla3