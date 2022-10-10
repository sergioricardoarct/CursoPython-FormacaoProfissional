# 1 - Crie um única string que contêm seu nome e sobrenome, em seguida use o
# slicing para separar o nome em uma variável e o seu sobrenome em outra.
# Printe esses valores.

var1= 'SergioRicardo'
nome= var1[:6]
sobrenome= var1[6:]

print(nome,sobrenome,sep=' ')

# 2 - Leia uma string através do input e retire o ultimo caractere.

var2=input('Nome:')

remove= var2[:-1]
print(remove)

# 3 - Faça um programa que leia uma string através do input e diga se
# ela possui uma vogal.

var3=input('Nome:')
vogal=("a" in var3) or("e" in var3) or("i" in var3) or("o" in var3) or("u" in var3)
print('Possue Vogal?', vogal)

# 4 - Faça um programa que insira a palavra 'ABC' na primeira posição
# de uma string lida por input.
var3=input('Nome:')
texto= "Abc"+var3
print(texto)