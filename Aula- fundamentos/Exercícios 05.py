# ir ao mercado sim ou nao#

faltacomida= False
sabado=True

vouaomercado=faltacomida or sabado
print('preciso ir ao mercado?', vouaomercado)

#sinal vermelho #

sinalverme= False
carrodadireita=True
carrodaesquerda=False

atravesar= sinalverme and not carrodadireita and not carrodaesquerda
print("posso atravesar com segunraça", atravesar)

# ou atravesar#

sinalverme= False
carrodadireita=True
carrodaesquerda=False

atravesar= sinalverme or not carrodadireita or not carrodaesquerda
print("posso atravesar com segunraça", atravesar)
