#Usando dicionários para implementar matrizes, escreva um programa que leia as notas das 5 provas de 5 alunos e armazene-as em uma matriz e calcule e imprima as médias das 5 notas de cada um dos 5 alunos. Calcule ainda a maior média e a quantidade de alunos com média maior ou igual a 7. 
notas = {}
media_notas = {}
maior_sete = 0
maior = 0
for x in range(5):
    for y in range(5):
        notas[x,y] = float(input(f'Digite a {y+1}° nota: '))
    print()


soma = 0
for x in range(5):
    for y in range(5):
        soma += notas[x,y]
    media = soma / 5
    media_notas[f'Media Aluno {x+1}'] = media
    soma = 0

for media in media_notas.values():
    if media > maior:
        maior = media
    if media >= 7:
        maior_sete += 1

print(f'Quantidade de média maiores que 7: {maior_sete}')
print(f'Maior média: {maior}')
for alunos in media_notas.items():
    print(alunos)
