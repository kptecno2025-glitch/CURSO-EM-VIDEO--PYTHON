soma_idade = 0
maior_idade = 0
nome_mais_velho = ''
contador_mulheres = 0

for c in range(4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: ')).upper().strip()

    soma_idade += idade

    if sexo == 'M' or sexo == 'MASCULINO':
        if idade > maior_idade:
            maior_idade = idade
            nome_mais_velho = nome

    elif (sexo == 'F' or sexo == 'FEMININO') and idade < 20:
        contador_mulheres += 1


media = int(soma_idade / 4)

print(f'A média de idade é {media}')
print(f'O homem mais velho é o {nome_mais_velho}')
print(f'Tem {contador_mulheres} mulheres com menos de 20 anos')