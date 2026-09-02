filmsTuple = ("Inception", "The Shawshanks Redemption",
             "The Drak knight", "Pulp Fiction", "Interistelar")
print(type(filmsTuple))

# 1 - Buscar os dois primeiros itens da tupla
print(filmsTuple[:2])

# 2 - Buscar o ultimo item da tupla
print(filmsTuple[-1])

# 3 - Buscar determinada posicao
print(filmsTuple[:3])

# 4 - Buscar filmes de uma posicao em diante
print(filmsTuple[3:])

# 5 - Recuperar um item da tupla pelo nome 
print(filmsTuple.index("Pulp Fiction"))