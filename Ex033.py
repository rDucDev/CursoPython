#3 numeros

a = int(input('Valor de A: '))
b = int(input('Valor de B: '))
c = int(input('Valor de C: '))


if a > b and a > c:
    print('A é o MAIOR')
else:
    if b > a and b > c:
        print('B é o MAIOR')
    else:
        print('C é o MAIOR')
if a < b and a < c:
    print('A É O MENOR')
else:
    if b < a and b < c:
        print('B É O MENOR')
    else:
        print('C É O MENOR')


