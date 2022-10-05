# len#
texto = input('Digite um texto:')
carct = 0

for i in texto:
    if (texto != ' '):
        carct += 1
print(carct)

# fatorial#

fatorial = int(input('Digite um texto:'))
valor = int(fatorial)
resultado=1
for i in range(1, fatorial + 1):
    resultado *= i

print(resultado)

#com texto#
leitura=int(input("quantos livros?"))
textofinal=' '
for x in range(leitura):
    textofinal += ', '+input("Livro:")

print("Serão esses livros:"+ textofinal)

