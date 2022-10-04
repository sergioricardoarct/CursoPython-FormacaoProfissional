#slicing#
var1= 'SergioRicardo'
nome= var1[:6]
sobrenome= var1[6:]

print(nome,sobrenome,sep=' ')

#remoção de utimo valor#

var2=input('Nome:')

remove= var2[:-1]
print(remove)

#Vogal#

var3=input('Nome:')
vogal=("a" in var3) or("e" in var3) or("i" in var3) or("o" in var3) or("u" in var3)
print('Possue Vogal?', vogal)

# abc#
var3=input('Nome:')
texto= "Abc"+var3
print(texto)