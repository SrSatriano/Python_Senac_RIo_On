'''1. Contagem regressiva: escreva um programa que peça ao usuário um número inteiro positivo 
e exiba uma contagem regressiva até 1, usando um loop while.
'''

num = int(input("Digite um número: "))

if num > 0:
    for i in range(num, 0, -1):
        print(i)
else:
    print("Número inválido. Digite um número inteiro positivo.")