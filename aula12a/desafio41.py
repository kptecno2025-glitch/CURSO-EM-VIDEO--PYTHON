ano = int(input('Digite o ano de nascimento: '))
idade = 2026 - ano

if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANCIA')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade == 20:
    print('SENIOR')
else:
    print('MASTER')
