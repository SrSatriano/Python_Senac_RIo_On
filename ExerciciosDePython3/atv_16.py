'''
Apresentando Membros da Família: crie uma função `family_members(**kwargs)` 
que recebe nomes de membros da família como argumentos nomeados e imprime suas relações.
'''

def membros_da_familia(**kwargs):
    for membro, relacao in kwargs.items():
        print(f"{membro} é {relacao} da família.")

membros_da_familia(pai="pai", mae="mãe", filho="filho", filha="filha", tio="tio", tia="tia", avo="avô", avo2="avó")
membros_da_familia(pai="pai", mae="mãe", filho="filho", filha="filha")
