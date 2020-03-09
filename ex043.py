peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso /(alt ** 2)
if imc <= 18.5:
    print('Abaixo do peso, seu IMC é {}'.format(imc))
elif 18.5 <= imc and imc <= 25:
    print ('O IMC é {:.2f}, Peso ideal'.format(imc))
elif 25 <= imc   and imc <=30:
    print ('O IMC é {:.1f}, Peso é Sobrepeso'.format(imc))
elif 30 <= imc and imc <= 40:
    print('O IMC é {:.1f}, Peso é Obesidade'.format(imc))
else:
    print('Obesidade Morbida {:.1f}'.format(imc))
