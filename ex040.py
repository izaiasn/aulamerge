nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
soma = ((nota1 + nota2) / 2)
if soma >= 5 and soma < 6:
    print ('Ixi foi para recuperação, sua média é: {:.1f} '.format(soma))
elif soma > 6:
    print ('Parabens foi aprovado, sua média é: {:.1f} '.format(soma))

else:
    print('Foi reprovado , sua média é: {:.1f} '.format(soma))
