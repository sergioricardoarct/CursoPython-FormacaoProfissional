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



#Senha#

senhausada=input("Senha:")
senha='1234'

print('A senha correta?', senhausada == senha)