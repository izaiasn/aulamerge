lista = []


def insert_nome(lista):
    nome = input('Digite um nome: ')
    lista.append(nome)
    return lista


def procurar_nome(lista, pos):
    try:
        if pos != 0:
            raise IndexError
    except IndexError:
        print('Indice não existe')
    else:
        return (lista[pos])


z = insert_nome(lista)
pos = int(input('Digite o número do indice: '))
w = procurar_nome(lista, pos)
if pos == 0:
    print(w)
