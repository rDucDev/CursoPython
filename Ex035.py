#Dá pra montar triangulo?

print('Informe tres retas do triangulo')
a = int(input('Comprimento do triangulo A: '))
b = int(input('Comprimento do triangulo B: '))
c = int(input('Comprimento do triangulo C: '))

if a > b+c or b > a+c or c > a+b:
    print('Não dá pra formar triangulo')
else:
    print('Dá pra montar triangulo')