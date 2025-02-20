'''
Contagem de Palavras em uma Frase: crie uma função `word_count(sentence)` 
que recebe uma string e retorna a quantidade de palavras nela.
'''

def contar_palavras(frase):
    return len(frase.split())

frase = input("Digite uma frase: ")
print("A frase possui", contar_palavras(frase), "palavras.")
