ano = int(input('Qual o ano de nascimento do jovem: '))
idade = 2026 - ano
if idade > 18:
    print('Já passou do tempo do alisatamento')
elif idade == 18:
    print('Já é hora de se alistar')
else:
    print('Ele ainda vai se alistar')
prazo = idade - 18
print(f'O prazo de alistamento é de {prazo} anos')