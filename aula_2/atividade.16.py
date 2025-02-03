# Exercício 16
# Alerta Climático: pergunte se está chovendo e se há previsão de raios.
# - Se estiver chovendo e houver previsão de raios, exiba "Fique em casa!".
# - Se apenas um dos fatores for verdadeiro, exiba "Cuidado ao sair".
# - Caso contrário, exiba "Pode sair com segurança".


chovendo = input("Está chovendo? ")
tem_raios = input("Tem previsão de raios? ")

if chovendo == "sim" and tem_raios == "sim":
    print("Fique em casa!")

elif chovendo == "sim" or tem_raios == "sim":
    print("Cuidado ao sair.")

else:
    print("Pode sair com segurança.")   