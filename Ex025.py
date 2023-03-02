#Procurando uma string dentro de outra

x = str(input('Digite o nome: '))
temsilva = x.split()
print('Tem SILVA no nome? {}'.format('silva' in x.lower()))