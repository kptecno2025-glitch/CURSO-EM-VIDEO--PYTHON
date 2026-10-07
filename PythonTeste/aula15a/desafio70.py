print('_'*40)
loja = 'LOJA SUPER BARATÃO'
print(f'{loja:^30}')
print('_'*40)
soma = cont = barato = primeiro = 0

while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    primeiro += 1
    if primeiro == 1:
        barato = preço
        prodbar = produto
    else:
        if preço < barato:
            barato = preço
            prodbar = produto


    soma += preço
    if preço > 1000:
        cont += 1
    opção = str(input('Quer continuar? [S/N] ')).strip().upper()
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opção == 'N':
        break

print(f'''O total da compra foi R${soma:.2f}
Temos {cont} produtos custando mais de R$1000.00
O produto mais barato foi {prodbar} que custa R${barato:.2f}''')
