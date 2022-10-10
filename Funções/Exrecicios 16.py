# bolean#

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

#def com possição#

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

# * arg#

def tipo (*args):
    for i in args:
        print(type(i))

tipo(1,13,1.5, "aslkd", True)

# decoretion#

def cita(func):
    def inner(str):
        return ('"'+ func(str).lower()+'"')
    return inner

@cita
def trasf(str):
    return str

print('E disse joao', trasf('askdjlk') )

#recursiva#

def printa(num):
    if num==11:
        return
    print(num//3)
    printa(num+1)
print(2)
