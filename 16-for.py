# Lista de filmes 
movieList = ["Inception", "The Shawshanks Redemption",
             "The Drak knight", "Pulp Fiction"]


# 1 - Iterando valores de uma lista 
for movie in movieList:
    print(movie)

# 2 - Quando a condicao for atendida o loop sera encerrado
for movie in movieList:
    if movie == "The Drak knight":
        break
    print(movie)

# 3 - Quando a condicao for atendida o loop vai para a proxima interacao 
for movie in movieList:
    if movie == "The Shawshanks Redemption":
        continue
    print(movie)

# 4 - Avaliacao do filme 
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliacoes deseja fazer:\n"))

total = 0
for i in range(movieRating):
    note = float(input("Digite a nota para o filme:\n"))
    total += note
if movieRating > 0:
    average = total / movieRating
else:
    average = 0 

print(f"Media de avaliacao do filme {movieName} e: {average:.2f}")