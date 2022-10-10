#Objetos#

objetos={
    'cadeira': 'sentar',
    'monitor': 'ver',
    'mouse': 'mecher'
}

procurado= input("o que voce procura").strip()
if procurado in objetos:
    print(objetos[procurado])
else:
    print("Não encontrado na lista")

#linsta negativa#
list=[ x for x in range(-30,-20)]
print(list)

#divisivel por 4 #

lista=[ x for x in range (4,101) if  x % 4== 0]
print(lista)

#filtro#

num=[ x for x in range(0,101) if x %10==0]
print(num)

num=[ x for x in range(0,101) if str(x)[-1]=='0']
print(num)


#array#

lista2=['0' if str(x)[-1]=='0' else '-' for x in range(0,21)]
print(lista2)