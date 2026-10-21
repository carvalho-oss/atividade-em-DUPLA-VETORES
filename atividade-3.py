import os
os.system ('cls')

numeros = []
QUANTIDADE_NUMERICA = 10
maioral = 0

for i in range(QUANTIDADE_NUMERICA):
    numero = int(input(f'Digite o seu {i+1}° número: '))
    if numero > 10:
        maioral += 1
    numeros.append(numero)

soma = sum(numeros)

print()
print('\n==== EXIBINDO VALORES ===')
print(f'soma {soma}')
print(f'Maiores que o número 10: {maioral}')