from datetime import datetime
pessoa = {}
pessoa['nome']=str(input('Nome: '))
ano=int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - ano
ctps=int(input('Carteira de trabalho (0 não tem): '))
pessoa['ctps'] = ctps
if ctps > 0:
    pessoa['contratação']=int(input('Ano de contratação: '))
    pessoa['salario']=float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - datetime.now().year)
print('-='*30)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
