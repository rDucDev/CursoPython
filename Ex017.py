#c2=a2+b2.
import math
a = float(input('Cumprimento do cateto adjacente: '))
b = float(input('Cumprimento do cateto oposto: '))
h2 = (a*a)+(b*b)
h = math.sqrt(h2)
hi= math.hypot(a,b)
print('Hipotenusa é {:.2f}'.format(h))
