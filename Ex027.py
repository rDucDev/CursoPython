#Mostrando primeiro e ultimo nome

x = input('Informe um nome completo: ')
dividido = x.split()
print('Bem-vindo(a), {}'.format(x))
print('Seu primeiro nome é {}'.format(dividido[0]))
print('Seu ultimo nome é {}'.format(dividido[len(dividido)-1]))


