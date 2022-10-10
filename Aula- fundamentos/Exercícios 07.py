# 1 - Crie um programa que leia por input dois números e realize
# a divisão entre ambos. Formate o print para mostrar o cálculo completo.
var1=int( input('Diga o primerio valor:').strip())
var2= int(input('Diga o primerio valor:').strip())

calculo= var1/var2
print('O valor da divisão é %.2f'%(calculo))

# 2 - Crie um programa que mostre o dia, mês, ano, hora,
# minuto e segundos inseridos pelo usuário. Formate o valor.
dia=input('Diga o dia:').strip()
mes=input('Diga o mes:').strip()
ano=input('Diga o ano:').strip()
hora=input('Diga a hora:').strip()
minu=input('Diga o minuto:').strip()
seg=input('Diga o segundo:').strip()

print('%s/%s/%s/ as %s:%s:%s' %(dia,mes,ano,hora,minu,seg))