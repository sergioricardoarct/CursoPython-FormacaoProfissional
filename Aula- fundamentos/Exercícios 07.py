#input convertido de string para int com saida formatada#
var1=int( input('Diga o primerio valor:').strip())
var2= int(input('Diga o primerio valor:').strip())

calculo= var1/var2
print('O valor da divisão é %.2f'%(calculo))

#data e hora#
dia=input('Diga o dia:').strip()
mes=input('Diga o mes:').strip()
ano=input('Diga o ano:').strip()
hora=input('Diga a hora:').strip()
minu=input('Diga o minuto:').strip()
seg=input('Diga o segundo:').strip()

print('%s/%s/%s/ as %s:%s:%s' %(dia,mes,ano,hora,minu,seg))