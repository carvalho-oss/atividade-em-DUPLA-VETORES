import os
os.system("cls")

print("Feito por: Yasmin")
print("R.A.: 026.087924")

vetor_temperatura = []

for i in range(7):
    temperatura = float(input("Registre a temperatura em ordem cronologica (SEG A DOM): "))
    vetor_temperatura.append(temperatura)
    
temperatura_max = max(vetor_temperatura)
temperatura_min = min(vetor_temperatura)
soma = sum(vetor_temperatura)
media = soma / 3

print(" = EXIBINDO VALORES = ")
for valor in vetor_temperatura:
    print("Temperaturas: ", valor)
print("Temperatura Maxima: ",temperatura_max)
print("Temperatura Minima: ",temperatura_min)
print("Média da Semana: ",media)
