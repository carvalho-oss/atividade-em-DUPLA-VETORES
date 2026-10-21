import os
os.system("cls")

contador = 0
vetor_nome = []
vetor_salario = []

for i in range(2):
    nome = str(input(f"Digite o nome do {i + 1}º funcionário: "))
    vetor_nome.append(nome)
    salario = float(input(f"Digite o salário de {nome} em R$: "))
    vetor_salario.append(salario)

if vetor_salario[i] > 2000:
    contador += 1

maior = max(vetor_salario)
pos = vetor_salario.index(maior)

print("Maior salário: ", vetor_nome[pos])
print("Salário: ", maior)
print("Ganham acima de R$ 2000: ", contador)