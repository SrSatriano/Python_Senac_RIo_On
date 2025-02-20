'''
3. Adivinhe o número: o programa deve gerar um número aleatório entre 1 e 6
e pedir para o usuário adivinhar. Ele deve continuar pedindo até o usuário acertar.
'''

import random

num = random.randint(1, 6)

while True:
    chute = int(input("Digite um número entre 1 e 6: "))
    if chute == num:
        print("Parabéns, você acertou!")
        break
    else:
        print("Tente novamente!")