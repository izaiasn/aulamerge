r1 = float(input(' 1 segmento: '))
r2 = float(input('2 Seguimento: '))
r3 = float(input('3 Seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Os segmentos podem formar Triangulo ', end='')
    if r1 == r2 == r3:
        print ('Equilatero')
    elif r1 != r2 != r3 != r1:
        print ('Escaleno')
    else:
        print ('Isosceles')
else:
    print ('Os segmentos não pode ser triangulo')