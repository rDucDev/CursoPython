import math

ang = float(input('Digite o angulo: '))
se = math.sin(math.radians(ang))
cos= math.cos(math.radians(ang))
tan= math.tan(math.radians(ang))

print('Seno: {:.2f}, \nCoseno: {:.2f}\n15Tangente: {:.2f}.'.format(se,cos,tan))