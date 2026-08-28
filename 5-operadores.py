num1 = int(input("Digite o primeiro numero \n"))
num2 = int(input("Digite o segundo numero \n "))



#aritimeticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2


print("O valor da soma e : ",sum)
print("O valor da subtracao e : ", sub)
print("O valor da divisao e :", div)
print("O valor da multiplicacao e : ", mult)

print(f"Potencia do numero {num1} por {num2} e : {exp}")
print(f"resto da divisao de  {num1} por {num2} e : {mod}")

# Comparacao
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
differrent = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"Os numeros  {num1} e {num2} sao iguais ? : {equal}")
print(f"Os numeros  {num1} e maior ou igual  {num2}?  : {bigger_equal}")