# Lista de cores ANSI (fundo colorido com texto preto)
c = (
    "\033[m",  # 0 - Sem cor (padrão do sistema)
    "\033[0;30;42m",  # 1 - Fundo Verde
    "\033[0;30;44m",  # 2 - Fundo Azul
    "\033[7;30m",  # 3 - Fundo Branco (Invertido)
    "\033[0;30;41m",  # 4 - Fundo Vermelho
)
def ajuda(com):
    titulo(f'Acessando o manual do comando {com}', 2)
    print(c[3], end='')
    help(com)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print("~" * tam)
    print(f'{msg}')
    print("~" * tam)
    print(c[0], end='')
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    questão = str(input('Função ou Biblioteca > ')).strip().lower()
    if questão == 'fim':
        titulo('ATÉ LOGO!', 4)
        break
    else:
        ajuda(questão)
