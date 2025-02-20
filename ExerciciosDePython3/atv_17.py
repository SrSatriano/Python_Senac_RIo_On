'''
Pedido de Restaurante: crie uma função `order_food(**kwargs)` que recebe itens de um pedido 
de restaurante como argumentos nomeados e imprime os pratos e suas quantidades.
'''

def pedido_restaurante(**kwargs):
    for prato, quantidade in kwargs.items():
        print(f"{quantidade} x {prato}")


pedido_restaurante(pizza=2, cerveja=4, batata_frita=1, hambúrguer=2)
pedido_restaurante(pizza=1, cerveja=1)