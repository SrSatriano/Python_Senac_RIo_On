# Exercício 11
# Idade para Votar e Dirigir: solicite a idade do usuário e informe:
# - Se ele é menor de idade.
# - Se pode votar mas não dirigir.
# - Se pode votar e dirigir.

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade.")

elif idade >= 16 and idade < 18:
    print("Pode votar mas não dirigir.")

else:
    print("Pode votar e dirigir.")  