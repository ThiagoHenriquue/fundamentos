movieList = ["Inception", "The Shawshanks Redemption",
             "The Drak knight", "Pulp Fiction"]

# 1 - Iterando valores de uma lista de filmes usando o while
index = 0
while index < len(movieList):
    print(movieList[index])
    index += 1

# 2 - Quando a condicao for atendida, o loop sera encerrado
index = 0
while index < len(movieList):
    if movieList[index] == "The Drak knight":
        break
    print(movieList[index])
    index += 1

# 3 - Quando a condicao for atendida, o loop vai para a proxima interacao
index = 0
while index < len(movieList):
    if movieList[index] == "The Drak knight":
        index +=1
        continue
    print(movieList[index])
    index += 1

# 4 - Avaliacao do filme com while
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliacoes deseja fazer:\n"))
total = 0
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filme:\n"))
    total += note
    count += 1

if movieRating > 0:
     average = total / movieRating
else:
     average = 0 

print(f"Media de avaliacao do filme {movieName} e: {average:.2f}")