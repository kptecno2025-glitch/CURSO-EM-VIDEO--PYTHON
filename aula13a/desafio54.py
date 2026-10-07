from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(7):
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = atual - nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f'Total de maiores: {maiores}')
print(f'Total de menores: {menores}')