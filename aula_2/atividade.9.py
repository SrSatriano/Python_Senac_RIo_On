# Exercício 09
# Verificação de número positivo, negativo ou zero: solicite ao usuário que
# insira um número. Verifique e exiba se o número é positivo, negativo ou é zero.

num = int(input("Digite um número: "))

if num > 0:
    print(f"O número {num} é positivo.")

elif num < 0:
    print(f"O número {num} é negativo.")

else:
    print(f"O número {num} é zero.")    