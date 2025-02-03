# Exercício 02
# Conversão de temperatura: solicite ao usuário que insira uma temperatura em
# Celsius, converta e exiba em Fahrenheit. Dica: °F = (°C x 9 ÷ 5) + 32

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("A temperatura em Fahrenheit é: {:.2f}".format(fahrenheit))