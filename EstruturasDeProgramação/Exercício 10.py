# salario devedor#

salario = float(input('Qual o seu salário:').strip())
divida = 250

if divida >= salario:
    devendo = divida - salario
    print('Voce tem saldo devedor e sua divida é de %.2f' % (devendo))
else:
    saldo = salario - divida
    print('voce não deve nada seu saldo é %.2f' % (saldo))

# CPF e Senha#


senha = input('Sua senha').strip()

CPFsalvo = 123456789
senhasalva = "abcde"

if senha == senhasalva:
    print("Seu Cpf é esse %d" % (CPFsalvo))

# idade#
idade = int(input("sua idade é: ").strip())

if idade <= 3:
    print('Você é um bebe')
elif idade >= 13:
    print('Você é uma criança')
elif idade >= 18:
    print('Você é um adolecente')
elif idade >= 65:
    print('Você é um adulto')

# calculadora

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
