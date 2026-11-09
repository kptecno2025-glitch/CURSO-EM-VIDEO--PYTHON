from datetime import date
def voto(nasc):
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATORIO'
    elif idade >= 70:
        return f'Com {idade} anos: VOTO OPICIONAL'



print(voto(int(input('Digite o ano de nascimento: '))))





