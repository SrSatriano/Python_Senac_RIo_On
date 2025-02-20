'''
Conversão de Temperatura: crie uma função `celsius_to_fahrenheit(c)` que recebe 
uma temperatura em graus Celsius e retorna o valor convertido para Fahrenheit.
'''

def celsius_para_fahrenheit(c):
    f = c * 1.8 + 32
    return f

print(celsius_para_fahrenheit(0))