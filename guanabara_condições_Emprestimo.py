valor_c= float(input('Entre com o valor do Imovel : '))
salario= float(input('Entre com o salário; '))
entrada= float(input('Entre com o valor da entrada: '))
meses= int(input('Entre com a quantidade de meses: '))
jur= float(input('Entre com a taxa de juros '))
sal_por= salario - (salario*0.30) 
val_pres= ((valor_c-entrada) / meses)
calc= (val_pres* jur) + val_pres 
print('Valor de prestação', calc)
##print('Valor Salario', sal_por)

if sal_por < calc:
    print('EMPRESTIMO NEGADO')
else:
    print('EMPRESTIMO APROVADO')
