# Exercício 10
# Calculadora simples: solicite ao usuário que insira dois números. Em seguida,
# solicite ao usuário que escolha uma das operações: +, -, x ou ÷. Realize a
# operação escolhida e exiba o resultado.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, x ou ÷): ")

if operacao == "+":
    resultado = num1 + num2

elif operacao == "-":
    resultado = num1 - num2

elif operacao == "x":
    resultado = num1 * num2

elif operacao == "÷":
    resultado = num1 / num2

else:
    print("Operação inválida.")

print("O resultado da operação {} {} {} é {}".format(num1, operacao, num2, resultado))  