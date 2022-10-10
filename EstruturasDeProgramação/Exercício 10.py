# 1 - Crie um programa que receba o seu saldo bancário e o quanto você deve.
# Em seguida o programa deve dizer se você tem saldo positivo ou negativo.

salario = float(input('Qual o seu salário:').strip())
divida = 250

if divida >= salario:
    devendo = divida - salario
    print('Voce tem saldo devedor e sua divida é de %.2f' % (devendo))
else:
    saldo = salario - divida
    print('voce não deve nada seu saldo é %.2f' % (saldo))

# 2 - Crie um programa que possui uma variável que guarde seu CPF e que guarde
# uma senha de sua escolha. Em seguida receba por input uma senha do usuário.
# Caso a senha recebida seja a correta mostre o CPF,
# caso não diga que a senha esta incorreta.


senha = input('Sua senha').strip()

CPFsalvo = 123456789
senhasalva = "abcde"

if senha == senhasalva:
    print("Seu Cpf é esse %d" % (CPFsalvo))

# 3 - Crie um programa que fale sobre sua idade. As regras são as seguintes
# você deve receber por input sua idade, se você tiver ate três anos
# printe que é um bebe, ate 13 anos uma criança, ate 18 anos adolescente,
# até 65 adulto. Em nenhum deste casos é um idoso
idade = int(input("sua idade é: ").strip())

if idade <= 3:
    print('Você é um bebe')
elif idade >= 13:
    print('Você é uma criança')
elif idade >= 18:
    print('Você é um adolecente')
elif idade >= 65:
    print('Você é um adulto')

# 4 - Crie um programa que receba dois números, e também receba do usuário
# a operação que deve ser feita, as possibilidades são soma(+), subtração (-),
# divisão(/) e multiplicação(*).
# Realize a operação escolhida sobre os dois números.

num = float(input("numero1:").strip())
num2 = float(input("numero2:").strip())
opera = input("Qual a operação + ,-,*,/:" )

if (opera == '+'):
    print(num + num2)
if (opera == '-'):
    print(num - num2)
if (opera == '*'):
    print(num * num2)
if (opera == '/'):
    print(num / num2)
