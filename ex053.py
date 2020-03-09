tx = str(input('Digite uma frase para saber se ele é Palídromo: ')).strip().upper()
pal = tx.split()
junto = ''.join(pal)
print('Você Digitou a frase {}'.format(junto))
