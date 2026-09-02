filmsList = ["Inception", "The Shawshanks Redemption",
             "The Drak knight", "Pulp Fiction", "Interistelar"]

# 1 - Tamanho da lista 
print(len(filmsList))

# 2 - Recuperar um item da lista pelo indice 
print(filmsList.index("Interistelar"))

# 3 - Adicionar item ao final da lista
filmsList.append("The Lord of the rings")
print(filmsList)

# 4 - Ordenar a lista
filmsList.sort()
print(filmsList)

# 5 - Copiar os itens de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

# 6 - Remove todos os itens da lista
filmsList.clear()
print(filmsList)