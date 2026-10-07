a1 = int(input('Digite o primeiro termo: '))
razão = int(input('Razão da PA: '))
décimo = a1 + (10 - 1) * razão
for c in range(a1, décimo, razão):
    print(f'{c} ->', end=' ')
print('FIM')