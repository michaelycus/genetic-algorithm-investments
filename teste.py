# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *

# root = ttk.Window(themename="superhero")

# b1 = ttk.Button(root, text="Submit", bootstyle="success")
# b1.pack(side=LEFT, padx=5, pady=10)

# b2 = ttk.Button(root, text="Submit", bootstyle="info-outline")
# b2.pack(side=LEFT, padx=5, pady=10)

# root.mainloop()

lista = [
    ({"name": "ameixa", "preco": 5.50}, 10),
    ({"name": "morango", "preco": 2.50}, 15),
    ({"name": "morango", "preco": 3.50}, 20),
    ({"name": "ameixa", "preco": 5.50}, 30),
]

# Dicionário para acumular as quantidades
quantidades_totais = {}

# Itera sobre a lista e acumula as quantidades
for fruta, quantidade in lista:
    nome = fruta["name"]
    if nome in quantidades_totais:
        quantidades_totais[nome]["quantidade"] += quantidade
    else:
        quantidades_totais[nome] = {"fruta": fruta, "quantidade": quantidade}

# Converte o dicionário de volta para uma lista de tuplas
resultado = [(v["fruta"], v["quantidade"]) for v in quantidades_totais.values()]

print(resultado)
