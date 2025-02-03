# Exercício 04
# Verificação de número par ou ímpar: solicite ao usuário que insira um número
# inteiro, teste e exiba se o número é par ou ímpar.

num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"O número {num} é par.")

else:
    print(f"O número {num} é impar.")

