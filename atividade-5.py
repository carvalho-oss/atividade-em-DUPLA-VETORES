import os
os.system ('cls')

vetor_notas = []
QUANTIDADE_NOTAS = 5
acima = 0

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    vetor_notas.append(nota)
    if nota >= 7:
        acima += 1

soma = sum(vetor_notas)
media = soma / QUANTIDADE_NOTAS
for notas, notas in enumerate(vetor_notas, start=1):
    print(f'{notas}°notas : {notas}')
    print(f'QUANTIDADE DE PESSOAS ACIMA DA MÉDIA SETE: {acima}')