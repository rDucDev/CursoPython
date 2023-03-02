# ex 15 - aluguel de carros

d = int(input('Alugar por quantos dias? ' ))
km= float(input('KMs rodados: '))
pago = (d*60)+(km*0.15)

print('Seu aluguel rodando ficou em R${:.2f}'.format(pago))