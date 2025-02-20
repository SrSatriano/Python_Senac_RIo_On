'''
Inverter uma String: crie uma função `reverse_string(text)` 
que recebe uma string e retorna seu inverso.
'''

def inverter_string(texto):
    return texto[::-1]

texto = input("Digite uma frase: ")
print("A frase invertida é:", inverter_string(texto))