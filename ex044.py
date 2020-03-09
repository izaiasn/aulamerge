print ('{:=^40}'.format(' Lojas Izaba '))
print('''
[1] Para pagamento à vista
[2] Para pagamento à vista no credito
[3] Para pagamento em 2 vezes
[4] Para pagamento em 3 vezes
''')
op = int(input('Digite um forma de: '))
valor = float(input('Digite o valor da compra: R$'))
des10 = (10/100) * valor
des5 = (5/100) * valor
if op == 1:
    valor = valor - des10
    print ('O valor da compra com desconto é {:.1f} Reais'.format(valor))
elif op == 2:
    valor = valor - des5
    print ('O valor da compra com desconto é {:.1f} Reais'.format(valor))
elif op == 3:
    valor = valor / 2
    print ('O valor da compra é {:.1f} Reais em 2X'.format(valor))
else:
    parc = int(input('Digite a quantidade de parcelas: '))
    valor = (valor / parc) + des10
    print ('O valor da compra è {:.1f} Reais em 3X com juras de 10 %'.format(valor))
