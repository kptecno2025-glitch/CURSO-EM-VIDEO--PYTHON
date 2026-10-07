alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'{'No.':<4}{'NOME':<10}{'MEDIA':>8}')
print('_'*20)

for i, e in enumerate(alunos):
    print(f'{i:<4}{e[0]:<10}{e[2]:>8.1f}')
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 para parar): '))
    if opcao == 999:
        break
    if 0 <= opcao <= len(alunos) - 1:
        print(f'{alunos[opcao][0]}{alunos[opcao][1]}')
    else:
        print('Opcao invalida! Tente novamente.')
