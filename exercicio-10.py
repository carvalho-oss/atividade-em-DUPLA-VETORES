import os
os.system("cls")

vetor_idade = []
contador = 0

for i in range(5):
    idade = int(input(f"Digite a {i + 1}º idade: "))
    if idade >= 0:
        vetor_idade.append(idade)
    elif idade <=120:
        vetor_idade.append(idade)
    else:
        print("Valor Inválido: ")
        print(idade)


maior_idade = max(vetor_idade)
menor_idade = min(vetor_idade)

print(" = EXIBINDO VALORES = ")
print("Maior idade: ", maior_idade)
print("Menor idade: ", menor_idade)
print("Quantidade de maiores de idade: ", contador)