idade = int(input('Digite sua idade: '))
mi = 9
inf = 14
jun = 19
sen = 25

if idade >= 0 and idade <= 9:
    print ('Sua categoria é Mirim ')
elif idade > 9 and idade <= 14:
    print ('Sua categorai é Infantil')
elif idade > 14 and idade <= 19:
    print ('Sua idade é Junior')
elif idade > 19 and idade <= 25:
    print ('Sua idade é Senio')
else:
    print ('Sua idade é Master')
