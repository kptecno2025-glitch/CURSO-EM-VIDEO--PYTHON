maior = 0
menor = 0
for c in range(5):
    peso = float(input(f'Digite o peso da {c+1} pessoa: kg'))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso foi {maior}kg')
print(f'o menor peso foi {menor}kg')
