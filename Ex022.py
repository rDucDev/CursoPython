#Fatiando strings

Nome = input('Bota um nome aí: ')
NOME = Nome.upper()
nome = Nome.lower()
s = Nome.split()
junto = ''.join(s)

print('Nome Maiusculo fica: {}'.format(NOME))
print('Minusculo fica: {}'.format(nome))
print('O nome sem espaços fica: {}'.format(junto))
print('Comprimento do nome inteiro sem espaço: {}'.format(len(junto)))
print('Comprimento da primeira palavra: {}'.format(len(s[0])))