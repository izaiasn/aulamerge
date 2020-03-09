continua = True
while continua:
    try:
        x = int(input('Primeiro valor:'))
        y = int(input('Segundo valor:'))
        if y == 0:
            raise ZeroDivisionError
    except ValueError:
        print('O valor informado deve ser númerico')
    except ZeroDivisionError:
        print('Impossivel dividir por Zero')
    else:
        continua = False
z = x/y
print(' O resultado da divisão é: ', z)
