# 6 - Crie uma função receba uma string e uma letra do alfabeto.
# Retorne a quantidade de vezes que essa letra tem na string.
# Caso não ocorra nenhuma vez, retorne 0.
import datetime as datetime


def contar(texto, carc):
    return texto.count(carc)


print(contar("Casaduor casadso", 'a'))


# 7 (DESAFIO) - Crie uma função receba uma string e uma letra do alfabeto.
# Retorne uma lista contendo o índice de onde todas as ocorrências aparecem.

def encontar(texto, carct):
    indices = []
    indice = 0
    for char in texto:
        if (char == carct):
            indices.append(indice)
        indice += 1
        return indices


print(encontar('alskdjfsalkdfjsçldwqpoiasqwasqwas', 'as'))


# 8 - Crie uma função que receba o que foi digitado pelo usuário no chat e
# também uma lista contendo todas as palavras não permitidas a serem digitadas.
# Essa função então retornara o que foi digitado pelo usuário mas no lugar
# das palavras não permitidas retorna o caractere '*’.

def palavra(text, palavras):
    for palavra in palavras:
        if palavra in text:
            text = text.replace(palavra, "*")
    return text


text_usua = "não pode falar casadour nem camara no chat"
palavra_proibidas = ['casadour', 'camara']

print(palavra(text_usua, palavra_proibidas))


# 9 - Crie uma função que retorne verdadeiro se uma string é totalmente
# maiúscula ou totalmente minúscula.


def verdade(texto):
    return texto.islower() or texto.isupper()


print(verdade("aaaaaaa"))
print(verdade("bbbbbb"))
print(verdade("aaaaaB"))


# 10 - Crie uma função que receba uma lista de textos.
# Detecte quais os valores dessa lista são inteiros e em seguida transforme
# eles para um número do tipo inteiro. Todos esses valores encontrados
# serão retornados em uma nova lista que deve estar ordenada.

def listat(lista):
    listainteiros = []
    for item in lista:
        if item.isdecimal():
            listainteiros.append(int(item))
    listainteiros.sort()
    return listainteiros


lista = ['1', '7', '9', '168', '2']

print(listat(lista))

# 11 - Leia por input sua data de nascimento no formado Dia/Mês/Ano e
# mostre quantos dias você já viveu.

import datetime

dataent = input("dia/ mês/ ano")
datanas = datetime.datetime.strftime(dataent, '%d/%m/%Y')
datahoje = datetime.datetime.now()

diferenca = datahoje - datanas
print(diferenca)

# 12 - Leia por input sua próxima data de aniversario no formado Dia/Mês/Ano
# e mostre quantos dias faltam para seu próximo aniversario.

import datetime
proxima=input('Aniversario seguinte: dia/mes/ano')
dataaniv= datetime.datetime.strftime(proxima,'%d/%m/%Y')
dataago=datetime.datetime.now()
dataaniveproximo= dataaniv-dataago
print(dataaniveproximo.days)