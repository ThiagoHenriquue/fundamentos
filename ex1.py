#Ex1 :
#primeiro_nome = input("Digite o primeiro nome: \n ")
#segundo_nome = input("Digite o sobrenome: \n ")

#nome_formatado = f"{segundo_nome} {primeiro_nome}"
#print(nome_formatado)

# Ex2:
#texto = "Pytohn e muito interessante"
#palavras = texto.split()
#texto_invertido = " ".join(palavras[::-1])
#print(texto_invertido)

#Ex3 :
texto1 = "arara"
texto2 = "python"
# Remove espaco e deixa nome em minusculo 
texto1_format = texto1.lower().replace(" ", "")
texto2_format = texto2.lower().replace(" ", "")

# verifica se o texto original e igual ao seu reverso 
palindromo1 = texto1_format == texto1[::-1]
palindromo2 = texto2_format == texto2[::-1]

print(palindromo1)
print(palindromo2)