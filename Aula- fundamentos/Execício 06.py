# 1 - Crie um programa que possui uma variável do “tipo string”
# contendo um número que indique quanto você tem no banco.
# Em seguida desconte mil deste valor e mostre na saída do programa.

var1= "10000"
desc=1000

saldo= float(var1)-desc
print(saldo)

# 2 - Crie um programa que indique se seu saldo bancário esta zerado
# (valor lógico). Declare uma variável para guardar seu saldo bancário.

saldo1= 1000
zerado= not bool(saldo1)
print("esta zerado?", zerado)

# 3 - Crie um programa que contenha sua altura, mas deve somente mostrar
# a parte inteira de sua altura na saída do programa,
# pois queremos uma estimativa.

altura=1.73
alturaint= int(altura)
print(f"O inteiro da altura {altura} é {alturaint}")

