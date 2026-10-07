resp = 'S'
media = soma = quant = maior = menor = 0


while resp == 'S':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1

    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n


    resp = str(input('Quer continuar? [S/N] ')).upper()
media = soma / quant
print(f'Você digitou {quant} numeros e sua média foi {media}')
print(f'O maior numero foi {maior} e o menor foi {menor}')