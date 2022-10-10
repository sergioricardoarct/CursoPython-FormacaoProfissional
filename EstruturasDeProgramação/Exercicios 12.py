# 1 - Crie um programa que receba uma string por input e conte quantos
# caracteres ela têm, não leve em conta caracteres de espaço.
# Você não deve usar o len().
texto = input('Digite um texto:')
carct = 0

for i in texto:
    if (texto != ' '):
        carct += 1
print(carct)

# 2 - Crie um programa que faça o calculo do fatorial de um número.
# O fatorial a ser calculado deve ser recebido por input.

fatorial = int(input('Digite um texto:'))
valor = int(fatorial)
resultado=1
for i in range(1, fatorial + 1):
    resultado *= i

print(resultado)

# 3 - Crie um programa que leia um quantidade arbitraria de textos e
# concatene eles numa string única.
leitura=int(input("quantos livros?"))
textofinal=' '
for x in range(leitura):
    textofinal += ', '+input("Livro:")

print("Serão esses livros:"+ textofinal)

# 4 - Cria um programa que printe a tabuada da divisão de um número lido
# por input.

numero = int(input("Digite a tabuada de divisão desejada: "))
for num in range(1, 11):
    print("%d / %d = %f " % (num, numero, num / numero))

# 5 (DESAFIO) - Crie um programa que percorra os números de 3 até 30 e
# diga se o número é primo ou não.

for numero in range(3, 31):
    e_primo = True

    for num_teste in range(2, numero):
        if (numero % num_teste == 0):
            e_primo = False
            break

    if (e_primo):
        print("O número %d é primo" % (numero))
    else:
        print("O número %d não é primo " % (numero))