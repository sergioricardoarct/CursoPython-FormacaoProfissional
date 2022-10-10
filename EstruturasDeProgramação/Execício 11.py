# 1 - Crie um programa que receba 5 números e retorne
# a média aritmética entre esses números


soma = 0
lidos = 0

while lidos < 5:
    numimp = float(input('Valor:'))
    soma += numimp
    lidos += 1
media = soma / 5
print(f'Media = {media}')

# 2 - Crie um programa que receba 5 números, realiza a soma destes números,
# mas caso um destes números seja negativo não considere ele na soma.

soma = 0
lidos = 0
while lidos < 5:
    numimp = float(input('Valor:'))
    soma += numimp
    if lidos > 0:
        soma += numimp
        lidos += 1
    lidos += 1
media = soma / 5
print(f'Media = {media}')

soma = 0
lidos = 0

