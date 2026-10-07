soma_idade = 0
contador = 0

for c in range(3):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))

    soma_idade += idade

    if idade > 18:
        contador += 1

print(soma_idade)
print(contador)