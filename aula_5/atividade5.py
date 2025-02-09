'''
Crie duas coleções e escreva no terminal a combinação das duas coleções, por exemplo:
fruta = ['maçã', 'banana', 'abacate', 'uva']
cor = ['vermelha', 'amarela', 'verde', 'roxa']

Exemplo de saída:

Maçã é vermelha
Banana é amarela
'''

fruta = ['maçã', 'banana', 'abacate', 'uva']
cor = ['vermelha', 'amarela', 'verde', 'roxa']

for i in range(len(fruta)):
    print(f"{fruta[i]} é {cor[i]}")