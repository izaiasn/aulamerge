from datetime import date
atual = date.today().year
nasc = int(input('Digite sua data de nascimento: '))
idade = atual - nasc
print (' Você nasceu em {} e tem {} anos'.format(nasc, idade))
if idade < 18:
    print ('Vc ainda vai se alista volte outro ano')
elif idade == 18:
    print('Vc esta na idade de alistamento')
else:
    print('Vc passou da epoca de alistamento')