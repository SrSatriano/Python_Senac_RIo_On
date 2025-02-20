'''
Filtrar Números Pares e Ímpares: crie uma função `filter_numbers(*args, parity="even")` que recebe 
números variáveis e um argumento opcional `parity` (`"even"` ou `"odd"`, padrão `"even"`) para retornar 
apenas os números pares ou ímpares da lista.
'''

def filtrar_numeros(*args, paridade="par"):
    if paridade == "par":
        return [n for n in args if n % 2 == 0]
    return [n for n in args if n % 2 != 0]


print(filtrar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, paridade="par"))
print(filtrar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, paridade="impar"))