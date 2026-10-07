usuario = 's'.upper()
soma = 0
cont = 0


while usuario == 'S':
    n = int(input('Digite um numero: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    usuario = input('Deseja continuar?[S/N] ').upper()

media = soma / cont

print(soma)
print(cont)
print(media)
print(maior)
print(menor)