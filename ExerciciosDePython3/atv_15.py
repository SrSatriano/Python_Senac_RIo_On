'''
Criar um Dicionário de Configuração: crie uma função `config_settings(defaults={}, **kwargs)` que recebe um 
dicionário padrão e substitui as chaves com os valores passados via `**kwargs`.
'''

def configurar_configuracoes(padrao={}, **kwargs):
    padrao.update(kwargs)
    return padrao


configuracoes = {
    "idioma": "pt-br",
    "tema": "claro",
    "fonte": "Arial",
    "tamanho_fonte": 17
}

configuracoes = configurar_configuracoes(configuracoes, tema="claro", tamanho_fonte=14)

print(configuracoes)
