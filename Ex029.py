#radar eletrônico

vel = int(input('O carro está a qtos KMs/hr?? '))
excesso = vel - 80
if excesso > 0:
    print('Você passou do limite!! MULTA de R${},00!!'.format(excesso * 7))
else: print('Dentro da velocidade ;)')

print('\n===fim===')