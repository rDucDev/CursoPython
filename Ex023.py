#Ex023 - Lendo numero

x = int(input('Digite um numero com 4 algarismos inteiros: '))
unidades    = x // 1 % 10
dezenas     = x // 10 % 10
centenas    = x // 100 % 10
milhares    = x // 1000 % 10

print('Unidades: {}'.format(unidades))
print('Dezenas: {}'.format(dezenas))
print('Centenas: {}'.format(centenas))
print('Milhares: {}'.format(milhares))