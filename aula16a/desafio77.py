palavras = ('aprender', 'programar', 'linguagem','python',
            'curso','gratis','estudar','praticar',
            'trabalhar', 'mercado','programador','futuro')

vogais = 'aeiou'

for palavra in palavras:
    print(f'Na palavra {palavra} temos: ', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(f'{letra}', end = ' ')
    print()

