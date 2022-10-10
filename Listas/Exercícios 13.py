# Lista soma#
lista = [1, 10, 6, 7, 8, 10]
soma = 0
for x in lista:
    soma += x
print(soma)

#  valor incremetar#

lista2 = []
item = 0

for x in range(1, 101):
    lista2.append(x)
print(lista2)

# set#
lista3 = {30, 4, 43, 52, 65, -10}
lista4 = {43, 2, 4, 76, 32, 65, 3}

listaJuncao = lista3.union(lista4)
print(listaJuncao)

# mses#
meses= ('janeiro', 'fevereiro', 'março', 'maio')
nascido = int(input('em que voce nasceu:'))

print(f"voce nasceu em {meses[nascido - 1]} ")


#dias#

dias=[]
for x in range (1,32):
    dias.append(x)
nascimento= int(input('que dia voce nasceu:'))
dias.remove(nascimento)
print(dias)