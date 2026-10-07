import math
co = float(input('digite o comprimento do cateto oposto: '))
ca = float(input('digite o comprimento do cateto adjacente: '))

hipotenusa = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))