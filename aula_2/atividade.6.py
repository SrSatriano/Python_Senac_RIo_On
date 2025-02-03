# Exercício 06
# Cálculo de gastos: escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado pelo usuário, assim como a quantidade de dias
# pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$ 50,00 por dia e R$ 0,18 por km rodado.

dias = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos km foram percorridos? "))

preco_dia = dias * 50
preco_km = km * 0.18
preco_total = preco_dia + preco_km

print(f"O total a pagar é: R${preco_total}")