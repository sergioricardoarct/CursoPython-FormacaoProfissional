# b6 - Crie um função que receba uma lista de elementos e um valor qualquer. Em
# seguida retorne um booleano dizendo se o valor foi encontrado ou não na lista.

def cont(arry,item):
    for i in arry:
        if i == item:
            return True
    return False

arrs= [2,3.3, True, "casaduor", 4]
print(cont(arrs, 2))
print(cont(arrs, True))
print(cont(arrs, 4))
print(cont(arrs,"casaduor" ))

#7 - Crie um função que receba uma lista de elementos e um valor qualquer. Em
#seguida retorne um booleano dizendo se o valor foi encontrado ou não e também
#a posição onde foi encontrado.

def encortra(arry, item):
    for i in range(0,len(arry)):
        if arry[i] == item:
            return True,i
    return False, -1

arrs= [2,3.3, True, "casaduor", 4]
print(encortra(arrs, 2))
print(encortra(arrs, True))
print(encortra(arrs, 4))
print(encortra(arrs, 5))

# 8 - Crie uma função que recebe um número arbitrário de parâmetros. Em seguida
# diga qual o tipo de cada parâmetro

def tipo (*args):
    for i in args:
        print(type(i))

tipo(1,13,1.5, "aslkd", True)

# 9 - Crie uma função que receba um string, mas que possua um decorator para
# transforma-la em uma citação, ou seja você deve retornas strings entre aspas
# duplas, além disso transforme todos os caracteres para minúscula usando a
# função lower().

def cita(func):
    def inner(str):
        return ('"'+ func(str).lower()+'"')
    return inner

@cita
def trasf(str):
    return str

print('E disse joao', trasf('askdjlk') )

#10 - Cria uma função recursiva que itere os números de 0 até 10 e printe o
#resultado de sua divisão inteira com o número três.

def printa(num):
    if num==11:
        return
    print(num//3)
    printa(num+1)
print(2)
