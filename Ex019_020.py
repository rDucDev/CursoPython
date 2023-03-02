#sorteando aluno (ex019) & Apresentação (ex020)
import random
a = input('Nome do aluno A: ')
b = input('Nome do aluno B: ')
c = input('Nome do aluno C: ')
d = input('Nome do aluno D: ')
lista = [a,b,c,d]
s = random.choice(lista)
print('Aluno sorteado: {}'.format(s))

ap= random.sample(lista,k=4)
print('Ordem de apresentação: {}'.format(ap))
