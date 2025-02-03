# Exercício 15
# Cadastro Simples com Regras: peça ao usuário idade e renda mensal. Se a idade
# for maior que 18 ou a renda for maior que R$ 3000, ele poderá se cadastrar.
# Caso contrário, exiba "Cadastro não permitido".

idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal: "))

if idade > 18 or renda > 3000:
    print("Cadastro permitido.")

else:
    print("Cadastro nao permitido.")    