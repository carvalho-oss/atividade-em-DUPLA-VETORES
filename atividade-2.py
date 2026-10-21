import os
os.system ('cls')

vetor_temperaturas = []
QUANTIDADE_NUMERICA = 7

for i in range(QUANTIDADE_NUMERICA):
    temperaturas =float(input(f'Digite a temperatura do {i+1}° dia: '))
    vetor_temperaturas.append(temperaturas)

    media = sum(vetor_temperaturas) / QUANTIDADE_NUMERICA
    maior = max(vetor_temperaturas)
    menor = min(vetor_temperaturas)

print('\n=== RELATÓRIOS DE TEMPERATURA ===')
print('Temperaturas Registradas: {temperaturas}')
print(f"Média semanal: {media:.1f}°C")
print(f"Maior temperatura: {maior:.1f}°C")
print(f"Menor temperatura: {menor:.1f}°C")