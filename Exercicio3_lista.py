from random import randint 
lista = []
for item in range(10):
    lista.append(randint(1,9))
print (lista)
for i in range(1,7):
    print ('o número :' ,i,'aparece', lista.count(i),'vezes')
    
    


