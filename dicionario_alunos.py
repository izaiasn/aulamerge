notas = {}
for i in range(3):
    nome = input('Nome ')
    nota1 = float(input('Nota1 '))
    nota2 = float(input('Nota2 '))
    notas[nome] = [nota1, nota2]

#print(notas)


def calcular_media(notas, nome):
    soma = sum(notas[nome])
    media = soma/2
    return media


nome = input('Digite um nome: ')
media = calcular_media(notas, nome)
print('Media do aluno', media)
