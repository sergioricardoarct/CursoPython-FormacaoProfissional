# 1 - Crie uma lista com os seguintes números 1,10,6,7,8,10.
# Em seguida printe a soma destes números.
lista = [1, 10, 6, 7, 8, 10]
soma = 0
for x in lista:
    soma += x
print(soma)

# 2 - Cria uma lista e preencha ela com valores de 1 a 100.
# Em seguida printe esses valores.

lista2 = []
item = 0

for x in range(1, 101):
    lista2.append(x)
print(lista2)

# 3 - Crie duas listas com os seguintes valores 30,4,43,52,65,-10 e
# 43,2,4,76,32,65,3. Agora faça a junção dessas listas, mas se houverem valores
# repetidos entre ambas eles não podem repetir na lista unida.
lista3 = {30, 4, 43, 52, 65, -10}
lista4 = {43, 2, 4, 76, 32, 65, 3}

listaJuncao = lista3.union(lista4)
print(listaJuncao)

# 4 - Crie uma lista contendo o nome de todos os meses do ano.
# Em seguida receba por input o mês (número) em que você nasceu
# e mostre qual o nome do mês que você nasceu.
meses= ('janeiro', 'fevereiro', 'março', 'maio')
nascido = int(input('em que voce nasceu:'))

print(f"voce nasceu em {meses[nascido - 1]} ")


# 5 - Crie uma lista contendo todos dias (número) do mês em que você nasceu.
# Em seguida receba por input o dia (número) em que você nasceu e remova
# desta lista. Ao final mostre o conteúdo da lista.

dias=[]
for x in range (1,32):
    dias.append(x)
nascimento= int(input('que dia voce nasceu:'))
dias.remove(nascimento)
print(dias)