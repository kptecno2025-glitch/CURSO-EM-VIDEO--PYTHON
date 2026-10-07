pessoa = {}

pessoa['nome'] = str(input('Nome: '))

pessoa['media'] = float(input(f'Média de {pessoa["nome"]}: '))

if pessoa['media'] > 7:
    pessoa['situacao'] = 'Aprovado'
else:
    pessoa['situacao'] = 'Reprovado'
print(f'Nome é igual a {pessoa["nome"]}')
print(f'Média é igual a {pessoa["media"]}')
print(f'A situação é igual a {pessoa["situacao"]}')



