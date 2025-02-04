# Exercício 10
# Calculadora simples: solicite ao usuário que insira dois números. Em seguida,
# solicite ao usuário que escolha uma das operações: +, -, x ou ÷. Realize a
# operação escolhida e exiba o resultado.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n1 - Adição (+)\n2 - Subtração (-)\n3 - Multiplicação (×)\n4 - Divisão (÷)")
opcao = input("Escolha a operação (1/2/3/4): ")

if opcao == "1":
    resultado = num1 + num2
elif opcao == "2":
    resultado = num1 - num2
elif opcao == "3":
    resultado = num1 * num2
elif opcao == "4":
    resultado = num1 / num2 if num2 != 0 else "Erro: divisão por zero"
else:
    resultado = "Opção inválida"

print(f"\nResultado: {resultado}")