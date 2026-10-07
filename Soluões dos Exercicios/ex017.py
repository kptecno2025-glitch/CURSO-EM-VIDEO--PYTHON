'''import math
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))

hipotenusa =  math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

'''segunda forma'''
from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print('a hipotenusa vai medir {:.2f}'.format(hi))

'''sem módulo
co = float(input('comprimento do cateto oposto: '))
ca = float(input('coomprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))'''




