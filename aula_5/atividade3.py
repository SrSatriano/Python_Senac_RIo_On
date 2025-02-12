# O programa deve imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números pares.

numero = int(input("Digite um número: "))

for i in range(1, numero + 1):
    if i % 2 == 0:
        print(i)