# 5 numeros#

soma = 0
lidos = 0

while lidos < 5:
    numimp = float(input('Valor:'))
    soma += numimp
    lidos += 1
media = soma / 5
print(f'Media = {media}')

# 5 numeros positivo #

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

