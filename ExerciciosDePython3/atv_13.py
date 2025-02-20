'''
Exibir Informações de um Usuário: crie uma função `user_info(name, age, **kwargs)` 
que recebe um nome, idade e qualquer outro detalhe opcional (por exemplo, cidade, profissão, hobby). 
A função deve exibir essas informações formatadas.
'''

def informacoes_usuario(nome, idade, **kwargs):
    info = f"Nome: {nome}, Idade: {idade}"
    for chave, valor in kwargs.items():
        info += f", {chave.capitalize()}: {valor}"
    print(info)

informacoes_usuario("Matheus", 30, cidade="Rio de Janeiro", profissao="Programador", hobby="Fazer Trilhas")
informacoes_usuario("Maria", 27, cidade="Rio de Janeiro", profissao="Chefe de Cozinha")
