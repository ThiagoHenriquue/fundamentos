# 1 - Listando valores de 0 a 10 que sejam menor que 4 
listNumbers = [i for i in range(10) if i < 4 ]
print(listNumbers)

# Lista de filmes
movieList = ["Inception", "The Shawshanks Redemption",
             "The Drak knight", "Pulp Fiction"]


# 2 - Filmes que possuem a letra 'e' no titulo 
movieWithE = [movie for movie in movieList if 'e' in movie.lower()]
print(movieWithE)

# 3 - Filmes que eu assisti 
moviesWatched = [movie for movie in movieList if movie != "Inception"]
print(moviesWatched)

# 4 - Encontrando um filme pelo nome 
while True:
    searchName = input("Digite o nome do filme para buscar na lista (ou sair para encerrar):\n")
    if searchName.lower() == "sair":
        print("programa Encerrado")
        break

    foundMovies = [movie for movie in movieList if searchName.lower( ) in movie.lower()]
    if foundMovies:
        print(f"Filme(s) encontrado(s) com o nome : {searchName}:")
        for foundMovies in foundMovies:
            print(foundMovies)
    else:
        print(f"Nenhum filme foi encontrado com o nome {searchName}. Tente novamente!")