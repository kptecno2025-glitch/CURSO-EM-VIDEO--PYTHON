valor = float(input('Digite o valor do produto: R$'))

print('Escolha a condição de pagamento:')
print('1 - A Vista dinheiro/cheque: 10% de desconto')
print('2 - A Vista no cartão: 5% de desconto')
print('3 - 2x no cartão: preço normal')
print('4 - 3x ou mais no cartão: 20% de juros')

opcao = int(input('Sua opção: '))

if opcao == 1:
    desconto = valor - (valor * (10 / 100))
    print(f'Seu produto custa R${desconto:.2f}')
elif opcao == 2:
    desconto = valor - (valor * (5 / 100))
    print(f'Seu produto custa R${desconto:.2f}')
elif opcao == 3:
    preco_normal = valor / 2
    print(f'Seu produto custa R${preco_normal:.2f} por parcela')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = valor * (20 / 100)
    total = valor + juros
    parcela = total / parcelas
    print(f'Seu produto custa R${total:.2f} em {parcelas}x de R${parcela:.2f}')