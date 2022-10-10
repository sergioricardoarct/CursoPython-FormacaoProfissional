# 1 - Crie um programa que possui duas variáveis, uma recebe o ano
# em que estamos e a outra o ano em que você nasceu.
# Em seguida subtraia ambas para receber uma estimativa de quantos anos você tem.
# Mostre esse valor na saída do programa.

ano_nascimento=1983
ano_atual=2022
idade= ano_atual-ano_nascimento
print('minha idade atual é %d'%(idade))

# 2 - Crie um programa que faz a média aritmética entre três números.
# Estes números devem ser salvos em uma variável.
# Mostre esse valor na saída do programa.


num1= 10
num2= 25
num3=18.5

media=(num1+num2+num3)/3
print('A media aritimetica e %.2f'%(media))

# 3 - Crie um programa que calcule o IMC (índice de massa corporal).
# O IMC é dado pelo peso em KG divido pela altura em metros elevado ao quadrado.
# Salvar esses valores em uma variável. Mostre esse valor na saída do programa.

peso=105
altura=1.73
imc= peso/(altura**2)
print('o imc é %.2d' %(imc))

# 4 (Desafio) - Você tem um determinado números de ovos de páscoa para dividir
# entre um determinado número de pessoas (duas variáveis iniciais).
# Determine quantos ovos ficarão por pessoa e quantos ovos sobrarão
# pois não puderam ser divido igualmente.
# Lembre que o número de ovos por pessoa é um número inteiro

ovos = 56
pessoas = 3
print("Tenho inicialmente %d ovos para %d pessoas " % (ovos, pessoas))
ovos_por_pessoas = ovos // pessoas
ovos_restantes = ovos % pessoas
print("Cada uma das %d pessoas terá %d ovo(s) " % (pessoas, ovos_por_pessoas))
print("Restou %d ovo(s) que não puderam ser divididos" % (ovos_restantes))
