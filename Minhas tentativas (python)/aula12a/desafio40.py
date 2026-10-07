nota = float(input('Qual a nota do aluno: '))

if nota < 5.0:
    print('REPROVADO!')
elif nota >= 5.0 and nota <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')