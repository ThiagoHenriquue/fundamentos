name = input("Digite o nome do filme :\n")
year_lauch = int(input("Digite o ano de lancamento do filme :\n"))
note_movie = float(input("Digite a nota do filme :\n"))



print("Dados do filme")
print("=========================")
#Alternativa 1
#print("nome do Filme:",name)
#print("ano de lancamento",year_lauch)
#print("nota do filme ",note_movie) 

#Alternativa 2

#print("nome do filme:", name, "\nAno de lancamento:", year_lauch, "\nNota do filme:", note_movie)

#Alternativa 3

print(f"Nome do jogo :{name}\n"
      f"Ano do lancamento:{year_lauch}\n"
      f"nota do filme:{note_movie}\n")