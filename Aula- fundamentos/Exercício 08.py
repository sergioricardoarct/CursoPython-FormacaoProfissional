# 1 - Crie um programa que responda se você foi aprovado numa prova.
# Você somente foi aprovado numa prova se sua média for maior ou igual que 7
# ou se sua nota no exame for maior ou igual a 5. Leia esses valores por input.

nota1= input("qual foi a primeira nota:")
nota2= input("qual foi a segunda nota:")

valor1=float(nota1)
valor2=float(nota2)

media= (valor1+valor2)/2

aprovado=(media>=7) or(media>=5)
print("Aprovado")

#
#if media >= 7:
#    print("Aprovado")
#else:
#    print("reprovado")
#



# 2 - Crie  um programa que diga se a senha esta correta e portanto você tem
# acesso ao sistema. A senha devera ser salva no código, e a tentativa deve ser
# lida por input.


senhausada=input("Senha:")
senha='1234'

print('A senha correta?', senhausada == senha)