'''
Escreva um programa que crie um dicionário com pelo menos 5 produtos e seus respectivos preços. 
Peça ao usuário o nome de um produto. Informe o preço caso o produto exista no dicionário, ou diga 
que o produto não foi encontrado.
'''

produtos = {
    "produto1": 10,
    "produto2": 20,
    "produto3": 30,
    "produto4": 40,
    "produto5": 50
}

nome_produto = input("Digite o nome do produto: ")

if nome_produto in produtos:
    print(produtos[nome_produto])
else:
    print("Produto nao encontrado")