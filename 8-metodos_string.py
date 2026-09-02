movieName = "Top Gun"
movieDescription = """
    Top Gun Maverick e um filme de aviacao e aventura muito 
    consagrado na industria
"""
print(movieName.upper())# tudo maiusculo 
print(movieName.lower())# tudo minusculo 
print(movieName.capitalize())# Primeira letra maiuscula
print(movieName.title()) # Primeira letra maiuscula
print(movieName.center(10, '-'))# Retorna a string centralizada com caractere de preenchimento 
print(movieName.find("u")) # posicao a posicao de um determinado caractere
print(movieName.find("o")) # conta caracteres
print(movieName.replace("Top", "Matrix"))# Altera elemento por outro
print(movieDescription.split(','))