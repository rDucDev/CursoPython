#Primeira e última ocorrência de uma string

x = str(input('Entre com uma frase: '))

print('Quantos As aparecem na frase?: {}'.format(x.lower().count('a')))
print('O primeiro A aparece na posição {}'.format(x.strip().lower().find('a')+1))
print('O ultimo A aparece na posição {}'.format(x.strip().lower().rfind('a')+1))