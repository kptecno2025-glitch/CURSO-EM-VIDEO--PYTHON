from random import sample
sorteado = tuple(sample(range(1, 11), 5))

print(f'Os valores sorteados foram: {sorteado}')

maior = max(sorteado)
print(f'O maior valor sorteado foi {maior}')

menor = min(sorteado)
print(f'O menor valor sorteado foi {menor}')