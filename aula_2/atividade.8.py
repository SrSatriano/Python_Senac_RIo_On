# Exercício 08
# Classificação de notas: solicite ao usuário que insira uma nota de 0 a 100 e
# atribua um conceito à nota, conforme o caso:
# - 90 ou mais → Nota A
# - 80 ou mais → Nota B
# - 70 ou mais → Nota C
# - 60 ou mais → Nota D
# - 50 ou mais → Nota E
# - Abaixo de 50 → Nota F  

nota = int(input("Digite uma nota de 0 a 100: "))

if nota >= 90:
    conceito = "A"

elif nota >= 80:
    conceito = "B"

elif nota >= 70:
    conceito = "C"

elif nota >= 60:
    conceito = "D"

elif nota >= 50:
    conceito = "E"

else:
    conceito = "F"

print(f"O conceito da nota é: {conceito}")