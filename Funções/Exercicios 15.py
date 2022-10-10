#1 - Crie uma função chamada “e_negativo” que receba um número,
#retorna um booleano “True” se o número for negativo, caso contrário
#retorna “False”.

def e_negativo(num):
    return num < 0


print(e_negativo(2))
print(e_negativo(-1))


#2 - Crie um função que receba um array de números (int ou float) e
#retorne sua soma.

def arrays(arr):
    soma = 0
    for i in arr:
        soma += i
    return soma


print(arrays([10, 30, 50]))


#3 - Crie um função que receba uma string e que conte e retorne o número
#de vogais desta string.

def vogaisa(texto):
    vogais = 0
    arrav = ('a', 'e', 'i', 'o', 'u')
    for i in texto:
        if i in arrav:
            vogais += 1
    return vogais


print(vogaisa("casadorudo"))

#4 - Crie um função que retorne o último caractere de um string recebida

def ulti(texto):
    return texto[len(texto)-1]

print(ulti("casadouert"))


#5 - Crie um função que receba dois números e uma string dizendo se deve
#realizar a soma ou subtração do números.

def cal(num1,num2,op):
    if (op=='+'):
        return (num1+num2)
    else:
        return (num1-num2)

print(cal(2,6,'-' ))