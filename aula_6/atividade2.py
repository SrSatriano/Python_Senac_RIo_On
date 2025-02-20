'''2. Somando números: crie um programa que peça números ao usuário e some-os. 
O programa deve parar de pedir números quando o usuário digitar 0, e então exibir a soma total.
'''

soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    soma += num
print(f'Soma total: {soma}')