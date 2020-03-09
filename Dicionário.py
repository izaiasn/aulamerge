produto = {"Sapato": 23,
           "Calças": 15,
           "Camisa": 51,
           "Blaser": 120}
for i, v in produto.items():
    if produto[i] > 50:
        print({i}, {v})
