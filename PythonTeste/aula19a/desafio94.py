grupo = []
while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str (input('Sexo [M/F]: ')).upper()
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa)
    resp = str(input('Quer continuar? [S/N]: ')).upper()
    if resp == 'N':
        break
print('-='*30)
quant = len(grupo)
print(f'O grupo tem {quant} pessoas')
media = sum(pessoa['idade'] for pessoa in grupo) / quant
print(f'A média de idade é de {media} anos')
mulheres = []
for pessoa in grupo:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
print(f'As mulheres cadastradas foram: {mulheres}')
superior = []
print('Lista de pessoas acima da média:')

for pessoa in grupo:
    if pessoa['idade'] > media:
        superior.append(pessoa)
        print(f'nome = {pessoa["nome"]}; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]}')

print('<< ENCERRADO >>')
