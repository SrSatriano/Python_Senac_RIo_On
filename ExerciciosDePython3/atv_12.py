'''
Multiplicação de Todos os Valores: crie uma função `multiply_all(*args)` 
que recebe uma quantidade variável de números e retorna o produto deles.
'''

def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

print(multiplicar_todos(1, 2, 3, 4, 5))
