def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


nome_jogador = str(input('Nome do Jogador: '))
gols_jogador = str(input('Gols do Jogador: '))

if gols_jogador.isnumeric() == True:
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0
if nome_jogador == '':
    ficha(gol=gols_jogador)
else:
    ficha(nome_jogador, gol=gols_jogador)




