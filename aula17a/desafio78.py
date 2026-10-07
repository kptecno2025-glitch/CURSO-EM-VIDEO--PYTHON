valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(f'Você digitou os valores: {valores}')

maior = max(valores)
menor = min(valores)

pos_maior = []
pos_menor = []
for p, v in enumerate(valores):
    if v == maior:
        pos_maior.append(p)
    elif v == menor:
        pos_menor.append(p)


print(f'O maior valor digitado foi {maior} na posição {pos_maior}')
print(f'O menor valor digitado foi {menor} na posição {pos_menor}')

