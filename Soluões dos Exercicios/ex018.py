import math
ang = float(input('digite o angulo que voce deseja: '))

rad = math.radians(ang)

sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print('o ângulo de {} tem o seno de {:.2f}'.format(ang, sen))
print('o ângulo de {} tem o cosseno de {:.2f}'.format(ang, cos))
print('o ângulo de {} tem a tangente de {:.2f}'.format(ang, tan))
