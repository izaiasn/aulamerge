produtos = {}
for i in range(5):
    nome = input('Nome')
    preco = float(input('Preço'))
    produtos[nome] = preco
print(produtos)

for i in produtos:
    if produtos[i] > 50:
        print(produtos[i])
