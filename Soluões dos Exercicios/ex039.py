from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} em {atual}')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento sera em {atual + (18 - idade)}')
elif idade > 18:
    print(f'Você ja deveria ter se alistado ha {idade - 18} anos')
    print(f'Seu alistamento foi em {atual - (idade - 18)}')
