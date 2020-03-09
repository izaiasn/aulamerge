



r1= float(input('Primeiro segmento: '))
r2= float(input('Segundo segmento: '))
r3= float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2<r1 + r3 and r3 < r1 +  r2:
    print (' Os segmentos podem formar um triangulo')
else:
    print ('Os seguimento Não podem formar triangulo')




#alistamento= int(input('Digite sua idade: '))
#anos= 18
#if alistamento == anos :
    #print ('Você está no prazo para alistamento')
#elif alistamento < anos :
    #falta= anos - alistamento
    #print('Você deve se alista daqui: ',falta,'Anos')
#else:
    #atrazo = alistamento - anos
    #print ('Você está atrasado em: ', atrazo, 'Anos')