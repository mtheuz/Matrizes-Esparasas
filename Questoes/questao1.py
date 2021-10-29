#Usando dicionários para implementar matrizes, escreva um programa que leia um número inteiro e uma matriz 4 x 4 de inteiros, e 
#obtenha uma segunda matriz resultado do produto da matriz original pelo número lido. Imprima a matriz resultado.
matriz = {}
num = int(input('Digite um numero: \n->'))

def mostra_matriz():
    for linha in range(4):
        for coluna in range(4):
            print(f' \t{matriz[linha,coluna]}',end='  ')
        print()
    print()

for x in range(4):
    for y in range(4):
        matriz[x,y] = int(input(f'Digite o {y+1}° número: '))
    print()
    
mostra_matriz()

for linha in range(4):
    for coluna in range(4):
        matriz[linha,coluna] = matriz[linha,coluna]*num

mostra_matriz()
    


        



