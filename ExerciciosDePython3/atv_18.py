'''
Criando um Perfil de Usuário: crie uma função `create_profile(**kwargs)` que recebe informações 
de um usuário (nome, idade, cidade, profissão, etc.) e retorna um dicionário com esses dados.
'''

def criar_perfil(**kwargs):
    return kwargs


perfil = criar_perfil(nome="Matheus", idade=30, cidade="Rio de Janeiro", profissao="Programador", hobby="Fazer Trilhas")
print(perfil)