# 1 - Crie uma função que retorne a subtração de dois elementos, mas que
# considere o valor absoluto deste valores.
import math


def sub(num1, num2):
    return (abs(num1) - abs(num2))


print(sub(200, 100))


# 2 – Sem usar “ifs”, crie uma função que receba dois números e retorne a soma
# dos mesmos, mas o valor retornado não pode passar de 10000 e deve ser
# sempre maior que 0.

def soma(num1, num2):
    soma = num1 + num2
    soma = min(10000, soma)
    soma = max(0, soma)
    return soma


print(soma(20, 20))
print(soma(5000, 6000))
print(soma(-10, 20))


# 3 (DESAFIO) - Crie uma função que receba argumentos de tamanho arbitrário.
# Todos esses argumentos serão números. Em seguida retorne o menor número
# entre todos os recebidos.

def menopr(*valor):
    menor = valor[0]
    for i in valor:
        menor = min(i, menor)
        return menor


print(menopr(10, 25, 6545, -5))

# 4 - Crie uma função que calcule a formula de Bhaskara, encontrado o X.
# Os coeficientes a,b e c devem ser lidos por input.

import math
a = float(input('Valor a:').strip())
b = float(input('Valor b:').strip())
c = float(input('Valor c:').strip())

x1 = (-b + math.sqrt(pow(b, 2) - 4 * a * c) / (2 * a))
x2 = (-b - math.sqrt(pow(b, 2) - 4 * a * c) / (2 * a))

print('A solução é', x1, x2)

# 5 - Crie uma função que receba uma string, e para cada letra minúscula a
# transforme em uma letra maiúscula e vice versa.

def trocar(texto):
    return texto.swapcase()

print(trocar('Ola Mundo'))

# 6 - Crie uma função receba uma string e uma letra do alfabeto.
# Retorne a quantidade de vezes que essa letra tem na string.
# Caso não ocorra nenhuma vez, retorne 0.


# 7 (DESAFIO) - Crie uma função receba uma string e uma letra do alfabeto.
# Retorne uma lista contendo o índice de onde todas as ocorrências aparecem.


# 8 - Crie uma função que receba o que foi digitado pelo usuário no chat e
# também uma lista contendo todas as palavras não permitidas a serem digitadas.
# Essa função então retornara o que foi digitado pelo usuário mas no lugar
# das palavras não permitidas retorna o caractere '*’.


# 9 - Crie uma função que retorne verdadeiro se uma string é totalmente
# maiúscula ou totalmente minúscula.


# 10 - Crie uma função que receba uma lista de textos.
# Detecte quais os valores dessa lista são inteiros e em seguida transforme
# eles para um número do tipo inteiro. Todos esses valores encontrados
# serão retornados em uma nova lista que deve estar ordenada.
