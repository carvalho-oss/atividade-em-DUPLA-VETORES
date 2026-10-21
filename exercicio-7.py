import os
os.system("cls")

vetor_numeros = []
vetor_positivos = []
contador = 0

for i in range(10):
    numero = int(input("Digite 10 números: "))
    if numero > 0:
        contador += 1
        vetor_positivos.append(numero)
    else:
        vetor_numeros.append(numero)

print("Números positivos: ", vetor_positivos)
print("Quantidade de números positivos: ", contador)