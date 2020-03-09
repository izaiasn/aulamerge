import ac1

s = ""
agenda = {}
print('''
[1] para inserir contato
[2] para remover contato
[3] para pesquisar
[4] para adicionar telefone
[5] para remover telefone
''')
while s != "sair":
    op = int(input('Digite uma das opções acima: '))
    if op == 1:
        nome = str(input('nome: '))
        telefone = str(input('telefone: '))
        print(ac1.adicionar_pessoa(agenda, nome, telefone))
    elif op == 2:
        nome = str(input('nome: '))
        print(ac1.remover_pessoa(agenda, nome))
    elif op == 3:
        nome = str(input('nome: '))
        print(ac1.pesquisar_pessoa(agenda, nome))
    elif op == 4:
        nome = str(input('nome: '))
        telefone = str(input('tel: '))
        print(ac1.adicionar_telefone(agenda, nome, telefone))
    elif op == 5:
        nome = str(input('nome: '))
        telefone = str(input('telefone: '))
        print(ac1.remover_telefone(agenda, nome, telefone))
    s = str(input(""))
