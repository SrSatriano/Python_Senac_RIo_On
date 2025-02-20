'''
Fatorial de um Número: crie uma função `factorial(n)` 
que recebe um número inteiro positivo e retorna seu fatorial.
'''
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

num = int(input("Digite um número: "))

print(f"O fatorial de {num} é: {fatorial(num)}")
