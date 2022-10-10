# def#

def e_negativo(num):
    return num < 0


print(e_negativo(2))
print(e_negativo(-1))


# arry#

def arrays(arr):
    soma = 0
    for i in arr:
        soma += i
    return soma


print(arrays([10, 30, 50]))


# String#

def vogaisa(texto):
    vogais = 0
    arrav = ('a', 'e', 'i', 'o', 'u')
    for i in texto:
        if i in arrav:
            vogais += 1
    return vogais


print(vogaisa("casadorudo"))

# ultima letra#

def ulti(texto):
    return texto[len(texto)-1]

print(ulti("casadouert"))


#calculador texto#

def cal(num1,num2,op):
    if (op=='+'):
        return (num1+num2)
    else:
        return (num1-num2)

print(cal(2,6,'-' ))