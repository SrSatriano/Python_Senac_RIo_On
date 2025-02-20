'''
Média de uma Lista de Números: crie uma função `average(numbers)` que recebe uma 
lista de números e retorna a média deles.
'''

def media(numeros):
    return sum(numeros) / len(numeros)

print(media([1, 2, 3, 4, 5]))