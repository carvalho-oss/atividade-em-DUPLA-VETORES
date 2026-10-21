import os
os.system("cls")

vetor_numero = []
novo_vetor_numero = []

for i in range(4):
    numero = int(input(f"Digite o {i + 1}º número: "))
    vetor_numero.append(numero)
    if numero % 2 == 0:
        novo_numero = 0
        novo_vetor_numero.append(novo_numero)
    else:
        novo_numero = 1
        novo_vetor_numero.append(novo_numero)

print(" = EXIBINDO VETORES = ")
print("Exibindo o vetor antes: ", vetor_numero)
print("Exibindo o vetor depois: ", novo_vetor_numero)

