'''
Escreva um programa que crie um dicionário com pelo menos 5 produtos e seus respectivos preços. 
Peça ao usuário o nome de um produto. Informe o preço caso o produto exista no dicionário, ou diga 
que o produto não foi encontrado.
'''

produtos = {
    "manga": 10,
    "feijao": 20,
    "refri": 30,
    "batata": 40,
    "bala": 50
}

nome_produto = input("Digite o nome do produto: ")

if nome_produto in produtos:
    print(produtos[nome_produto])
else:
    print("Produto nao encontrado")