filmsSet = {"Inception", "The Shawshanks Redemption",
             "The Drak knight", "Pulp Fiction", "Interistelar"}
print(type(filmsSet))


# 1 - Buscar o tamanho do set 
print(len(filmsSet))

# 2 - True e 1 sao considerados o mesmo valor 
exampleSet = {"Inception", True, 1, 8.7 }
print(exampleSet)

# 3 - Adicionar um item de outro set 
filmsSet.update(exampleSet)
print(filmsSet)

# 4 - Remover um item do set 
filmsSet.remove(True)
filmsSet.remove(8.7)
print(filmsSet)