# Verificando as primeiras letras de um texto

x = input('Nome de uma cidade: ')
xsplit = x.split()
primeiro = xsplit[0]
print('Nome da cidade começa com Santo?? {}'.format('SANTO' in primeiro.upper()))