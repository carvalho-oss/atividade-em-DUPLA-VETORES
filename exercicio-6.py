import os
os.system("cls")

vetor_a = []
vetor_b = []
vetor_c = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    vetor_a.append(numero)
for i in range(5):
    numero_segundo = int(input(f"Digite novamente outro {i + 1}º número: "))
    vetor_b.append(numero_segundo)

for i in range(5):
    soma = vetor_a[i] + vetor_b[i]
    vetor_c.append(soma)

print(" = EXIBINDO RESULTADOS = ")
print("Vetor A: ", vetor_a)
print("Vetor B: ", vetor_b)
print("Vetor C: ", vetor_c)