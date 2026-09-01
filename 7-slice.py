movieName = "Top Gun"

#string[inicio:fim] - indicve comeca na posicao 0 / indice final -1

# 1- Buscar toda a string a parti da primeira posicao
print(movieName[0:])

# 2- Buscar toda a string ate a ultima posicao
print(movieName[:7])

# 3 - Buscar toda a string da terceira ate a ultima posicao 
print(movieName[2:])

"""
string[inicio:fim:passo] 
indicve comeca na posicao 0 / indice final -1
passo - determina o incremento. por padrao esse numero e 1.
"""

# 4 - Buscar toda a string de 2 em 2 caracteres 
print(movieName[::2])

#5 - Buscar toda a string nos indices impares 
print(movieName[1::2])

# 6 - Inverter uma string de tras para frente
print(movieName[::-1])