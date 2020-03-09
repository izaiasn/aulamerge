# Atividade ContÃ­nua 01
# Aluno 01: Izaias N Souza
# Aluno 02: Antonio 
#Criando uma lista.


agenda = []


def option():
    print(''' 
    [1] Adicionar Contato
    [2] Remover Contato
    [3] Pesquisar contato
    [4] Adicionar Telefone
    [5] Remover Telefone)''')
    ##validacao = int(input('Escolha uma opção'))
    return validacao('Escolha uma opção abaixo', 1, 6)


while True:
     opcao = option()
     if opcao == 6:                     
         break
     elif opcao == 1:
         adicionar_pessoa() 
     elif opcao == 2:
         remover_pessoa() 
     elif opcao == 3:
         pesquisar_pessoa() 
     elif opcao == 4:
         adicionar_telefone() 
     elif opção == 5:
         remover_telefone()

def adicionar_pessoa():
    nome = a_nome
    telefone = a_telefone
    agenda.append([nome], [telefone])