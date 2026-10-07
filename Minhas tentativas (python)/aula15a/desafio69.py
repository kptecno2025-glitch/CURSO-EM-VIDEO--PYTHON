idade = cont = tot18 = hom = mul = 0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    if idade >= 18:
        tot18 += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if sexo == 'M':
        hom += 1
    if sexo == 'F' and idade < 20:
        mul += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    opção = str(input('Quer continuar? [S/N] ')).strip().upper()
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opção == 'N':
        break





print(f'''FIM DO PROGRAMA
Total de pessoas com mais de 18 anos: {tot18}
Ao todo temos {hom} homens cadastrados
E temos {mul} mulheres com menos de 20 anos''')


