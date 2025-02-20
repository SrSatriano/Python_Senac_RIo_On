'''
Contar Vogais em uma Palavra: crie uma função `count_vowels(word)` 
que recebe uma string e retorna a quantidade de vogais nela.
'''
def contar_vogais(palavra):
    return sum(1 for char in palavra if char in 'aeiouAEIOU')

palavra = input("Digite uma palavra: ")
print("A palavra possui", contar_vogais(palavra), "vogais.")

   