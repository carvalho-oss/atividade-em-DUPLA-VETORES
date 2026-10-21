import os
os.system (' cls')

numeros = []

for i in range(8):
    num = int(input(f'Digite o {i+1}° número inteiro: '))
    numeros.append(num)

alvo = int(input('\n Digite um número para a pesquisa: '))

if alvo in numeros:
    posicao = numeros.index(alvo)
    print(f"O número (alvo) existe e está na posição (índice) {posicao}.")
else:
    print("Número não encontrado.")