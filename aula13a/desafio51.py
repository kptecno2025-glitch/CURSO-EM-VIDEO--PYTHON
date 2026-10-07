a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

termo = a1

for c in range(10):
    print(termo, end=' ')
    termo += r

