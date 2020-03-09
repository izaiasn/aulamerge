# Atividade Contínua 01
# Aluno 01: Izais Nilson de Souza RA 1902195
# Aluno 02: Antonio Matos de Jesus 


def adicionar_pessoa(agenda, nome, telefone):
    ok = False
    valor = 0
    while True:
        ad = telefone
        if ad:
            valor = int(ad)
            ok = True
        else:
            print('Dados não incluido')
            return agenda
        if nome in agenda:
            return agenda
        else:
            insert = []
            insert.append(telefone)
            agenda[nome] = insert
            return agenda


def remover_pessoa(agenda, nome):
    if nome in agenda:
        agenda.pop(nome)
        return agenda
    else:
        return agenda


def pesquisar_pessoa(agenda, nome):
    pesquisa = []
    if nome in agenda:
        for i in agenda[nome]:
            pesquisa.append(i)
        return pesquisa
    else:
        return pesquisa


def adicionar_telefone(agenda, nome, telefone):
    ok = False
    valor = 0
    while True:
        ad = telefone
        if ad :
            valor = int()
            ok = True
        else:
            print('Dados não incluido')
            return agenda
        if nome in agenda:
            if telefone in agenda[nome]:
                return agenda
            else:
                agenda[nome].append(telefone)
                return agenda
        else:
            return agenda


def remover_telefone(agenda, nome, telefone):
    pesq = pesquisar_pessoa(agenda, nome)
    if nome in agenda:
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)
            return agenda
