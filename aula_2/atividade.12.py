# Exercício 12
# Login Simples: simule um sistema de login simples onde é solicitado um nome de
# usuário e senha. Se o nome for "admin" e a senha for "1234", exiba "Acesso
# permitido", caso contrário, exiba "Acesso negado".

nome = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if nome == "admin" and senha == "1234":
    print("Acesso permitido.")

else:
    print("Acesso negado.")