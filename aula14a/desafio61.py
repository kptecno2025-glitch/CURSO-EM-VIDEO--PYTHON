a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

termo = a1
pa = 1

while pa <= 10:
    print(termo, end=' ')
    termo += r
    pa += 1