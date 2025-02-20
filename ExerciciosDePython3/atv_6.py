'''
Números Primos: crie uma função `is_prime(n)` 
que recebe um número inteiro maior que 1 e retorna `True` se for primo e `False` caso contrário.
'''

def e_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Digite um número: "))

if e_primo(num):
    print(num, "é um número primo.")
else:
    print(num, "não é um número primo.")