# 6 - Escolha três objetos de sua escolha e em seguida cria uma lista para
# armazenar o objeto e sua função. Agora por input receba o nome desse objeto
# e imprima a sua função. Caso o objeto não exista, informa ao usuário.

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

# 7 - Crie uma lista contendo todos os números negativos de -30 até -20.
# Printe essa lista.
list=[ x for x in range(-30,-20)]
print(list)

# 8 - Percorra os números de 4 a 100 e mantenha apenas aqueles divisíveis por 4.

lista=[ x for x in range (4,101) if  x % 4== 0]
print(lista)

# 9 (DESAFIO) - Crie uma lista contendo todos os números de 0 a 100, mas filtre,
# mantendo apenas os números que terminam com 0.

num=[ x for x in range(0,101) if x %10==0]
print(num)

num=[ x for x in range(0,101) if str(x)[-1]=='0']
print(num)


# 10 - Percorra os números de 0 a 20 e crie um array, onde caso o número
# terminar com zero o valor devera ser '0', caso contrario devera ser '-'.

lista2=['0' if str(x)[-1]=='0' else '-' for x in range(0,21)]
print(lista2)