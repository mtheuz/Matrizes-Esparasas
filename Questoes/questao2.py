#Usando dicionários para implementar matrizes, escreva um programa que leia uma matriz 4x4 e encontre e imprima o maior e o menor elemento da matriz. 

matriz = {}
maior = 0
menor = 0

for linha in range(4):
    for coluna in range(4):
        matriz[linha,coluna] = int(input(f'{[linha,coluna]} <- '))

for linha in range(4):
    for coluna in range(4):
        if matriz[linha,coluna] > maior:
            maior = matriz[linha,coluna]

        if coluna == 0:
            menor = matriz[linha,coluna]

        elif matriz[linha,coluna] < menor:
            menor = matriz[linha,coluna]

print()
for linha in range(4):
    for coluna in range(4):
        print(f' {matriz[linha,coluna]}',end='  ')
    print()

print()
print(f'Maior valor = {maior}')
print(f'Menor valor = {menor}')
