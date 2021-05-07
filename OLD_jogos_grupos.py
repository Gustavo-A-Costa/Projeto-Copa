# Código por Gustavo Albuquerque - 20/04/2021
from sorteio import sorteio_copa
from placar import resultado


def fase_grupos():
    grupos = sorteio_copa()
    GA = grupos[0]
    GB = grupos[1]
    GC = grupos[2]
    GD = grupos[3]
    GE = grupos[4]
    GF = grupos[5]
    GG = grupos[6]
    GH = grupos[7]

    # ZERANDO OS PONTOS DO GRUPO A
    PA0, PA1, PA2, PA3 = 0, 0, 0, 0
    # ZERANDO OS PONTOS DO GRUPO B
    PB0, PB1, PB2, PB3 = 0, 0, 0, 0
    # ZERANDO OS PONTOS DO GRUPO C
    PC0, PC1, PC2, PC3 = 0, 0, 0, 0
    # ZERANDO OS PONTOS DO GRUPO D
    PD0, PD1, PD2, PD3 = 0, 0, 0, 0
    # ZERANDO OS PONTOS DO GRUPO E
    PE0, PE1, PE2, PE3 = 0, 0, 0, 0
    # ZERANDO OS PONTOS DO GRUPO F
    PF0, PF1, PF2, PF3 = 0, 0, 0, 0
    # ZERANDO OS PONTOS DO GRUPO G
    PG0, PG1, PG2, PG3 = 0, 0, 0, 0
    # ZERANDO OS PONTOS DO GRUPO H
    PH0, PH1, PH2, PH3 = 0, 0, 0, 0

    print('Grupo A:\n{}\n'.format(GA))
    print('Grupo B:\n{}\n'.format(GB))
    print('Grupo C:\n{}\n'.format(GC))
    print('Grupo D:\n{}\n'.format(GD))
    print('Grupo E:\n{}\n'.format(GE))
    print('Grupo F:\n{}\n'.format(GF))
    print('Grupo G:\n{}\n'.format(GG))
    print('Grupo H:\n{}\n'.format(GH))

    # Vou destacar as sel de seus grupos e dicionários para montar os duelos
    # Vou colocar índices - AXJY - Grupo A, Rod X, Jogo Y

    # ___________________GRUPO A___________________
    # Grupo A, rodada 1:
    print('\n JOGOS - GRUPO A \n')

    print('\n RODADA 1: \n')
    A1J1 = resultado(int(GA[0]['Nível']), int(GA[1]['Nível']))  # chamando (f)

    print('{} {} x {} {}'.format(GA[0]['País'],
          A1J1[0], A1J1[1], GA[1]['País']))

    # Estrutura de pontuação da partida:
    if A1J1[0] > A1J1[1]:
        PA0 = PA0 + 3
    elif A1J1[0] < A1J1[1]:
        PA1 = PA1 + 3
    else:
        PA0 = PA0 + 1
        PA1 = PA1 + 1
    # FIM DO JOGO 1
    A1J2 = resultado(int(GA[2]['Nível']), int(GA[3]['Nível']))

    print('{} {} x {} {}'.format(GA[2]['País'],
          A1J2[0], A1J2[1], GA[3]['País']))

    # Estrutura de pontuação da partida:
    if A1J2[0] > A1J2[1]:
        PA2 = PA2 + 3
    elif A1J2[0] < A1J2[1]:
        PA3 = PA3 + 3
    else:
        PA2 = PA2 + 1
        PA3 = PA3 + 1
    # FIM DO JOGO 2

    # Grupo A, rodada 2:
    print('\n RODADA 2: \n')
    A2J1 = resultado(int(GA[0]['Nível']), int(GA[2]['Nível']))

    print('{} {} x {} {}'.format(GA[0]['País'],
          A2J1[0], A2J1[1], GA[2]['País']))

    # Estrutura de pontuação da partida:
    if A2J1[0] > A2J1[1]:
        PA0 = PA0 + 3
    elif A2J1[0] < A2J1[1]:
        PA2 = PA2 + 3
    else:
        PA0 = PA0 + 1
        PA2 = PA2 + 1
    # FIM DO JOGO 1

    A2J2 = resultado(int(GA[1]['Nível']), int(GA[3]['Nível']))

    print('{} {} x {} {}'.format(GA[1]['País'],
          A2J2[0], A2J2[1], GA[3]['País']))

    # Estrutura de pontuação da partida:
    if A2J2[0] > A2J2[1]:
        PA1 = PA1 + 3
    elif A2J2[0] < A2J2[1]:
        PA3 = PA3 + 3
    else:
        PA1 = PA1 + 1
        PA3 = PA3 + 1
    # FIM DO JOGO 2

    # Grupo A, rodada 3:
    print('\n RODADA 3: \n')
    A3J1 = resultado(int(GA[0]['Nível']), int(GA[3]['Nível']))

    print('{} {} x {} {}'.format(GA[0]['País'],
          A3J1[0], A3J1[1], GA[3]['País']))

    # Estrutura de pontuação da partida:
    if A3J1[0] > A3J1[1]:
        PA0 = PA0 + 3
    elif A3J1[0] < A3J1[1]:
        PA3 = PA3 + 3
    else:
        PA0 = PA0 + 1
        PA3 = PA3 + 1
    # FIM DO JOGO 1

    A3J2 = resultado(int(GA[1]['Nível']), int(GA[2]['Nível']))

    print('{} {} x {} {}'.format(GA[1]['País'],
          A3J2[0], A3J2[1], GA[2]['País']))

    # Estrutura de pontuação da partida:
    if A3J2[0] > A3J2[1]:
        PA1 = PA1 + 3
    elif A3J2[0] < A3J2[1]:
        PA2 = PA2 + 3
    else:
        PA1 = PA1 + 1
        PA2 = PA2 + 1
    # FIM DO JOGO 2
    # SALDOS:
    gfA0 = A1J1[0] + A2J1[0] + A3J1[0]
    gsA0 = A1J1[1] + A2J1[1] + A3J1[1]

    gfA1 = A1J1[1] + A2J2[0] + A3J2[0]
    gsA1 = A1J1[0] + A2J2[1] + A3J2[1]

    gfA2 = A1J2[0] + A2J1[1] + A3J2[1]
    gsA2 = A1J2[1] + A2J1[0] + A3J2[0]

    gfA3 = A1J2[1] + A2J2[1] + A3J1[1]
    gsA3 = A1J2[0] + A2J2[0] + A3J1[0]

    tabelaGA = [[GA[0]['País'], PA0, gfA0, gsA0, gfA0 - gsA0],
                [GA[1]['País'], PA1, gfA1, gsA1, gfA1 - gsA1],
                [GA[2]['País'], PA2, gfA2, gsA2, gfA2 - gsA2],
                [GA[3]['País'], PA3, gfA3, gsA3, gfA3 - gsA3]]

    print('\n----GRUPO A----\n ')
    print('País    / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(tabelaGA[0], tabelaGA[1],
          tabelaGA[2], tabelaGA[3]))

    # _______________ FIM DO GRUPO A_______________________

    # ___________________GRUPO B___________________
    # Grupo B, rodada 1:
    print('\n JOGOS - GRUPO B \n')

    print('\n RODADA 1: \n')
    B1J1 = resultado(int(GB[0]['Nível']), int(GB[1]['Nível']))  # chamando (f)

    print('{} {} x {} {}'.format(GB[0]['País'],
          B1J1[0], B1J1[1], GB[1]['País']))

    # Estrutura de pontuação da partida:
    if B1J1[0] > B1J1[1]:
        PB0 = PB0 + 3
    elif B1J1[0] < B1J1[1]:
        PB1 = PB1 + 3
    else:
        PB0 = PB0 + 1
        PB1 = PB1 + 1
    # FIM DO JOGO 1
    B1J2 = resultado(int(GB[2]['Nível']), int(GB[3]['Nível']))

    print('{} {} x {} {}'.format(GB[2]['País'],
          B1J2[0], B1J2[1], GB[3]['País']))

    # Estrutura de pontuação da partida:
    if B1J2[0] > B1J2[1]:
        PB2 = PB2 + 3
    elif B1J2[0] < B1J2[1]:
        PB3 = PB3 + 3
    else:
        PB2 = PB2 + 1
        PB3 = PB3 + 1
    # FIM DO JOGO 2

    # Grupo 1, rodada 2:
    print('\n RODADA 2: \n')
    B2J1 = resultado(int(GB[0]['Nível']), int(GB[2]['Nível']))

    print('{} {} x {} {}'.format(GB[0]['País'],
          B2J1[0], B2J1[1], GB[2]['País']))

    # Estrutura de pontuação da partida:
    if B2J1[0] > B2J1[1]:
        PB0 = PB0 + 3
    elif B2J1[0] < B2J1[1]:
        PB2 = PB2 + 3
    else:
        PB0 = PB0 + 1
        PB2 = PB2 + 1
    # FIM DO JOGO 1

    B2J2 = resultado(int(GB[1]['Nível']), int(GB[3]['Nível']))

    print('{} {} x {} {}'.format(GB[1]['País'],
          B2J2[0], B2J2[1], GB[3]['País']))

    # Estrutura de pontuação da partida:
    if B2J2[0] > B2J2[1]:
        PB1 = PB1 + 3
    elif B2J2[0] < B2J2[1]:
        PB3 = PB3 + 3
    else:
        PB1 = PB1 + 1
        PB3 = PB3 + 1
    # FIM DO JOGO 2

    # Grupo 1, rodada 3:
    print('\n RODADA 3: \n')
    B3J1 = resultado(int(GB[0]['Nível']), int(GB[3]['Nível']))

    print('{} {} x {} {}'.format(GB[0]['País'],
          B3J1[0], B3J1[1], GB[3]['País']))

    # Estrutura de pontuação da partida:
    if B3J1[0] > B3J1[1]:
        PB0 = PB0 + 3
    elif B3J1[0] < B3J1[1]:
        PB3 = PB3 + 3
    else:
        PB0 = PB0 + 1
        PB3 = PB3 + 1
    # FIM DO JOGO 1

    B3J2 = resultado(int(GB[1]['Nível']), int(GB[2]['Nível']))

    print('{} {} x {} {}'.format(GB[1]['País'],
          B3J2[0], B3J2[1], GB[2]['País']))

    # Estrutura de pontuação da partida:
    if B3J2[0] > B3J2[1]:
        PB1 = PB1 + 3
    elif B3J2[0] < B3J2[1]:
        PB2 = PB2 + 3
    else:
        PB1 = PB1 + 1
        PB2 = PB2 + 1
    # FIM DO JOGO 2
    # SALDOS:
    gfB0 = B1J1[0] + B2J1[0] + B3J1[0]
    gsB0 = B1J1[1] + B2J1[1] + B3J1[1]

    gfB1 = B1J1[1] + B2J2[0] + B3J2[0]
    gsB1 = B1J1[0] + B2J2[1] + B3J2[1]

    gfB2 = B1J2[0] + B2J1[1] + B3J2[1]
    gsB2 = B1J2[1] + B2J1[0] + B3J2[0]

    gfB3 = B1J2[1] + B2J2[1] + B3J1[1]
    gsB3 = B1J2[0] + B2J2[0] + B3J1[0]

    tabelaGB = [[GB[0]['País'], PB0, gfB0, gsB0, gfB0 - gsB0],
                [GB[1]['País'], PB1, gfB1, gsB1, gfB1 - gsB1],
                [GB[2]['País'], PB2, gfB2, gsB2, gfB2 - gsB2],
                [GB[3]['País'], PB3, gfB3, gsB3, gfB3 - gsB3]]

    print('\n----GRUPO B----\n ')
    print('País    / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(tabelaGB[0], tabelaGB[1],
          tabelaGB[2], tabelaGB[3]))

    # _______________ FIM DO GRUPO B_______________________

    # ___________________GRUPO C___________________
    # Grupo C, rodada 1:
    print('\n JOGOS - GRUPO C \n')

    print('\n RODADA 1: \n')
    C1J1 = resultado(int(GC[0]['Nível']), int(GC[1]['Nível']))  # chamando (f)

    print('{} {} x {} {}'.format(GC[0]['País'],
          C1J1[0], C1J1[1], GC[1]['País']))

    # Estrutura de pontuação da partida:
    if C1J1[0] > C1J1[1]:
        PC0 = PC0 + 3
    elif C1J1[0] < C1J1[1]:
        PC1 = PC1 + 3
    else:
        PC0 = PC0 + 1
        PC1 = PC1 + 1
    # FIM DO JOGO 1
    C1J2 = resultado(int(GC[2]['Nível']), int(GC[3]['Nível']))

    print('{} {} x {} {}'.format(GC[2]['País'],
          C1J2[0], C1J2[1], GC[3]['País']))

    # Estrutura de pontuação da partida:
    if C1J2[0] > C1J2[1]:
        PC2 = PC2 + 3
    elif C1J2[0] < C1J2[1]:
        PC3 = PC3 + 3
    else:
        PC2 = PC2 + 1
        PC3 = PC3 + 1
    # FIM DO JOGO 2

    # Grupo C, rodada 2:
    print('\n RODADA 2: \n')
    C2J1 = resultado(int(GC[0]['Nível']), int(GC[2]['Nível']))

    print('{} {} x {} {}'.format(GC[0]['País'],
          C2J1[0], C2J1[1], GC[2]['País']))

    # Estrutura de pontuação da partida:
    if C2J1[0] > C2J1[1]:
        PC0 = PC0 + 3
    elif C2J1[0] < C2J1[1]:
        PC2 = PC2 + 3
    else:
        PC0 = PC0 + 1
        PC2 = PC2 + 1
    # FIM DO JOGO 1

    C2J2 = resultado(int(GC[1]['Nível']), int(GC[3]['Nível']))

    print('{} {} x {} {}'.format(GC[1]['País'],
          C2J2[0], C2J2[1], GC[3]['País']))

    # Estrutura de pontuação da partida:
    if C2J2[0] > C2J2[1]:
        PC1 = PC1 + 3
    elif C2J2[0] < C2J2[1]:
        PC3 = PC3 + 3
    else:
        PC1 = PC1 + 1
        PC3 = PC3 + 1
    # FIM DO JOGO 2

    # Grupo C, rodada 3:
    print('\n RODADA 3: \n')
    C3J1 = resultado(int(GC[0]['Nível']), int(GC[3]['Nível']))

    print('{} {} x {} {}'.format(GC[0]['País'],
          C3J1[0], C3J1[1], GC[3]['País']))

    # Estrutura de pontuação da partida:
    if C3J1[0] > C3J1[1]:
        PC0 = PC0 + 3
    elif C3J1[0] < C3J1[1]:
        PC3 = PC3 + 3
    else:
        PC0 = PC0 + 1
        PC3 = PC3 + 1
    # FIM DO JOGO 1

    C3J2 = resultado(int(GC[1]['Nível']), int(GC[2]['Nível']))

    print('{} {} x {} {}'.format(GC[1]['País'],
          C3J2[0], C3J2[1], GC[2]['País']))

    # Estrutura de pontuação da partida:
    if C3J2[0] > C3J2[1]:
        PC1 = PC1 + 3
    elif C3J2[0] < C3J2[1]:
        PC2 = PC2 + 3
    else:
        PC1 = PC1 + 1
        PC2 = PC2 + 1
    # FIM DO JOGO 2
    # SALDOS:
    gfC0 = C1J1[0] + C2J1[0] + C3J1[0]
    gsC0 = C1J1[1] + C2J1[1] + C3J1[1]

    gfC1 = C1J1[1] + C2J2[0] + C3J2[0]
    gsC1 = C1J1[0] + C2J2[1] + C3J2[1]

    gfC2 = C1J2[0] + C2J1[1] + C3J2[1]
    gsC2 = C1J2[1] + C2J1[0] + C3J2[0]

    gfC3 = C1J2[1] + C2J2[1] + C3J1[1]
    gsC3 = C1J2[0] + C2J2[0] + C3J1[0]

    tabelaGC = [[GC[0]['País'], PC0, gfC0, gsC0, gfC0 - gsC0],
                [GC[1]['País'], PC1, gfC1, gsC1, gfC1 - gsC1],
                [GC[2]['País'], PC2, gfC2, gsC2, gfC2 - gsC2],
                [GC[3]['País'], PC3, gfC3, gsC3, gfC3 - gsC3]]

    print('\n----GRUPO C----\n ')
    print('País    / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(tabelaGC[0], tabelaGC[1],
          tabelaGC[2], tabelaGC[3]))

    # _______________ FIM DO GRUPO C_______________________
    # ___________________GRUPO D___________________
    # Grupo D, rodada 1:
    print('\n JOGOS - GRUPO D \n')

    print('\n RODADA 1: \n')
    D1J1 = resultado(int(GD[0]['Nível']), int(GD[1]['Nível']))  # chamando (f)

    print('{} {} x {} {}'.format(GD[0]['País'],
          D1J1[0], D1J1[1], GD[1]['País']))

    # Estrutura de pontuação da partida:
    if D1J1[0] > D1J1[1]:
        PD0 = PD0 + 3
    elif D1J1[0] < D1J1[1]:
        PD1 = PD1 + 3
    else:
        PD0 = PD0 + 1
        PD1 = PD1 + 1
    # FIM DO JOGO 1
    D1J2 = resultado(int(GD[2]['Nível']), int(GD[3]['Nível']))

    print('{} {} x {} {}'.format(GD[2]['País'],
          D1J2[0], D1J2[1], GD[3]['País']))

    # Estrutura de pontuação da partida:
    if D1J2[0] > D1J2[1]:
        PD2 = PD2 + 3
    elif D1J2[0] < D1J2[1]:
        PD3 = PD3 + 3
    else:
        PD2 = PD2 + 1
        PD3 = PD3 + 1
    # FIM DO JOGO 2

    # Grupo D, rodada 2:
    print('\n RODADA 2: \n')
    D2J1 = resultado(int(GD[0]['Nível']), int(GD[2]['Nível']))

    print('{} {} x {} {}'.format(GD[0]['País'],
          D2J1[0], D2J1[1], GD[2]['País']))

    # Estrutura de pontuação da partida:
    if D2J1[0] > D2J1[1]:
        PD0 = PD0 + 3
    elif D2J1[0] < D2J1[1]:
        PD2 = PD2 + 3
    else:
        PD0 = PD0 + 1
        PD2 = PD2 + 1
    # FIM DO JOGO 1

    D2J2 = resultado(int(GD[1]['Nível']), int(GD[3]['Nível']))

    print('{} {} x {} {}'.format(GD[1]['País'],
          D2J2[0], D2J2[1], GD[3]['País']))

    # Estrutura de pontuação da partida:
    if D2J2[0] > D2J2[1]:
        PD1 = PD1 + 3
    elif D2J2[0] < D2J2[1]:
        PD3 = PD3 + 3
    else:
        PD1 = PD1 + 1
        PD3 = PD3 + 1
    # FIM DO JOGO 2

    # Grupo D, rodada 3:
    print('\n RODADA 3: \n')
    D3J1 = resultado(int(GD[0]['Nível']), int(GD[3]['Nível']))

    print('{} {} x {} {}'.format(GD[0]['País'],
          D3J1[0], D3J1[1], GD[3]['País']))

    # Estrutura de pontuação da partida:
    if D3J1[0] > D3J1[1]:
        PD0 = PD0 + 3
    elif D3J1[0] < D3J1[1]:
        PD3 = PD3 + 3
    else:
        PD0 = PD0 + 1
        PD3 = PD3 + 1
    # FIM DO JOGO 1

    D3J2 = resultado(int(GD[1]['Nível']), int(GD[2]['Nível']))

    print('{} {} x {} {}'.format(GD[1]['País'],
          D3J2[0], D3J2[1], GD[2]['País']))

    # Estrutura de pontuação da partida:
    if D3J2[0] > D3J2[1]:
        PD1 = PD1 + 3
    elif D3J2[0] < D3J2[1]:
        PD2 = PD2 + 3
    else:
        PD1 = PD1 + 1
        PD2 = PD2 + 1
    # FIM DO JOGO 2
    # SALDOS:
    gfD0 = D1J1[0] + D2J1[0] + D3J1[0]
    gsD0 = D1J1[1] + D2J1[1] + D3J1[1]

    gfD1 = D1J1[1] + D2J2[0] + D3J2[0]
    gsD1 = D1J1[0] + D2J2[1] + D3J2[1]

    gfD2 = D1J2[0] + D2J1[1] + D3J2[1]
    gsD2 = D1J2[1] + D2J1[0] + D3J2[0]

    gfD3 = D1J2[1] + D2J2[1] + D3J1[1]
    gsD3 = D1J2[0] + D2J2[0] + D3J1[0]

    tabelaGD = [[GD[0]['País'], PD0, gfD0, gsD0, gfD0 - gsD0],
                [GD[1]['País'], PD1, gfD1, gsD1, gfD1 - gsD1],
                [GD[2]['País'], PD2, gfD2, gsD2, gfD2 - gsD2],
                [GD[3]['País'], PD3, gfD3, gsD3, gfD3 - gsD3]]

    print('\n----GRUPO D----\n ')
    print('País    / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(tabelaGD[0], tabelaGD[1],
          tabelaGD[2], tabelaGD[3]))

    # _______________ FIM DO GRUPO D_______________________
    # ___________________GRUPO E___________________
    # Grupo E, rodada 1:
    print('\n JOGOS - GRUPO E \n')

    print('\n RODADA 1: \n')
    E1J1 = resultado(int(GE[0]['Nível']), int(GE[1]['Nível']))  # chamando (f)

    print('{} {} x {} {}'.format(GE[0]['País'],
          E1J1[0], E1J1[1], GE[1]['País']))

    # Estrutura de pontuação da partida:
    if E1J1[0] > E1J1[1]:
        PE0 = PE0 + 3
    elif E1J1[0] < E1J1[1]:
        PE1 = PE1 + 3
    else:
        PE0 = PE0 + 1
        PE1 = PE1 + 1
    # FIM DO JOGO 1
    E1J2 = resultado(int(GE[2]['Nível']), int(GE[3]['Nível']))

    print('{} {} x {} {}'.format(GE[2]['País'],
          E1J2[0], E1J2[1], GE[3]['País']))

    # Estrutura de pontuação da partida:
    if E1J2[0] > E1J2[1]:
        PE2 = PE2 + 3
    elif E1J2[0] < E1J2[1]:
        PE3 = PE3 + 3
    else:
        PE2 = PE2 + 1
        PE3 = PE3 + 1
    # FIM DO JOGO 2

    # Grupo E, rodada 2:
    print('\n RODADA 2: \n')
    E2J1 = resultado(int(GE[0]['Nível']), int(GE[2]['Nível']))

    print('{} {} x {} {}'.format(GE[0]['País'],
          E2J1[0], E2J1[1], GE[2]['País']))

    # Estrutura de pontuação da partida:
    if E2J1[0] > E2J1[1]:
        PE0 = PE0 + 3
    elif E2J1[0] < E2J1[1]:
        PE2 = PE2 + 3
    else:
        PE0 = PE0 + 1
        PE2 = PE2 + 1
    # FIM DO JOGO 1

    E2J2 = resultado(int(GE[1]['Nível']), int(GE[3]['Nível']))

    print('{} {} x {} {}'.format(GE[1]['País'],
          E2J2[0], E2J2[1], GE[3]['País']))

    # Estrutura de pontuação da partida:
    if E2J2[0] > E2J2[1]:
        PE1 = PE1 + 3
    elif E2J2[0] < E2J2[1]:
        PE3 = PE3 + 3
    else:
        PE1 = PE1 + 1
        PE3 = PE3 + 1
    # FIM DO JOGO 2

    # Grupo E, rodada 3:
    print('\n RODADA 3: \n')
    E3J1 = resultado(int(GE[0]['Nível']), int(GE[3]['Nível']))

    print('{} {} x {} {}'.format(GE[0]['País'],
          E3J1[0], E3J1[1], GE[3]['País']))

    # Estrutura de pontuação da partida:
    if E3J1[0] > E3J1[1]:
        PE0 = PE0 + 3
    elif E3J1[0] < E3J1[1]:
        PE3 = PE3 + 3
    else:
        PE0 = PE0 + 1
        PE3 = PE3 + 1
    # FIM DO JOGO 1

    E3J2 = resultado(int(GE[1]['Nível']), int(GE[2]['Nível']))

    print('{} {} x {} {}'.format(GE[1]['País'],
          E3J2[0], E3J2[1], GE[2]['País']))

    # Estrutura de pontuação da partida:
    if E3J2[0] > E3J2[1]:
        PE1 = PE1 + 3
    elif E3J2[0] < E3J2[1]:
        PE2 = PE2 + 3
    else:
        PE1 = PE1 + 1
        PE2 = PE2 + 1
    # FIM DO JOGO 2
    # SALDOS:
    gfE0 = E1J1[0] + E2J1[0] + E3J1[0]
    gsE0 = E1J1[1] + E2J1[1] + E3J1[1]

    gfE1 = E1J1[1] + E2J2[0] + E3J2[0]
    gsE1 = E1J1[0] + E2J2[1] + E3J2[1]

    gfE2 = E1J2[0] + E2J1[1] + E3J2[1]
    gsE2 = E1J2[1] + E2J1[0] + E3J2[0]

    gfE3 = E1J2[1] + E2J2[1] + E3J1[1]
    gsE3 = E1J2[0] + E2J2[0] + E3J1[0]

    tabelaGE = [[GE[0]['País'], PE0, gfE0, gsE0, gfE0 - gsE0],
                [GE[1]['País'], PE1, gfE1, gsE1, gfE1 - gsE1],
                [GE[2]['País'], PE2, gfE2, gsE2, gfE2 - gsE2],
                [GE[3]['País'], PE3, gfE3, gsE3, gfE3 - gsE3]]

    print('\n----GRUPO E----\n ')
    print('País    / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(tabelaGE[0], tabelaGE[1],
          tabelaGE[2], tabelaGE[3]))

    # _______________ FIM DO GRUPO E_______________________
    # ___________________GRUPO F___________________
    # Grupo F, rodada 1:
    print('\n JOGOS - GRUPO F \n')

    print('\n RODADA 1: \n')
    F1J1 = resultado(int(GF[0]['Nível']), int(GF[1]['Nível']))  # chamando (f)

    print('{} {} x {} {}'.format(GF[0]['País'],
          F1J1[0], F1J1[1], GF[1]['País']))

    # Estrutura de pontuação da partida:
    if F1J1[0] > F1J1[1]:
        PF0 = PF0 + 3
    elif F1J1[0] < F1J1[1]:
        PF1 = PF1 + 3
    else:
        PF0 = PF0 + 1
        PF1 = PF1 + 1
    # FIM DO JOGO 1
    F1J2 = resultado(int(GF[2]['Nível']), int(GF[3]['Nível']))

    print('{} {} x {} {}'.format(GF[2]['País'],
          F1J2[0], F1J2[1], GF[3]['País']))

    # Estrutura de pontuação da partida:
    if F1J2[0] > F1J2[1]:
        PF2 = PF2 + 3
    elif F1J2[0] < F1J2[1]:
        PF3 = PF3 + 3
    else:
        PF2 = PF2 + 1
        PF3 = PF3 + 1
    # FIM DO JOGO 2

    # Grupo F, rodada 2:
    print('\n RODADA 2: \n')
    F2J1 = resultado(int(GF[0]['Nível']), int(GF[2]['Nível']))

    print('{} {} x {} {}'.format(GF[0]['País'],
          F2J1[0], F2J1[1], GF[2]['País']))

    # Estrutura de pontuação da partida:
    if F2J1[0] > F2J1[1]:
        PF0 = PF0 + 3
    elif F2J1[0] < F2J1[1]:
        PF2 = PF2 + 3
    else:
        PF0 = PF0 + 1
        PF2 = PF2 + 1
    # FIM DO JOGO 1

    F2J2 = resultado(int(GF[1]['Nível']), int(GF[3]['Nível']))

    print('{} {} x {} {}'.format(GF[1]['País'],
          F2J2[0], F2J2[1], GF[3]['País']))

    # Estrutura de pontuação da partida:
    if F2J2[0] > F2J2[1]:
        PF1 = PF1 + 3
    elif F2J2[0] < F2J2[1]:
        PF3 = PF3 + 3
    else:
        PF1 = PF1 + 1
        PF3 = PF3 + 1
    # FIM DO JOGO 2

    # Grupo F, rodada 3:
    print('\n RODADA 3: \n')
    F3J1 = resultado(int(GF[0]['Nível']), int(GF[3]['Nível']))

    print('{} {} x {} {}'.format(GF[0]['País'],
          F3J1[0], F3J1[1], GF[3]['País']))

    # Estrutura de pontuação da partida:
    if F3J1[0] > F3J1[1]:
        PF0 = PF0 + 3
    elif F3J1[0] < F3J1[1]:
        PF3 = PF3 + 3
    else:
        PF0 = PF0 + 1
        PF3 = PF3 + 1
    # FIM DO JOGO 1

    F3J2 = resultado(int(GF[1]['Nível']), int(GF[2]['Nível']))

    print('{} {} x {} {}'.format(GF[1]['País'],
          F3J2[0], F3J2[1], GF[2]['País']))

    # Estrutura de pontuação da partida:
    if F3J2[0] > F3J2[1]:
        PF1 = PF1 + 3
    elif F3J2[0] < F3J2[1]:
        PF2 = PF2 + 3
    else:
        PF1 = PF1 + 1
        PF2 = PF2 + 1
    # FIM DO JOGO 2
    # SALDOS:
    gfF0 = F1J1[0] + F2J1[0] + F3J1[0]
    gsF0 = F1J1[1] + F2J1[1] + F3J1[1]

    gfF1 = F1J1[1] + F2J2[0] + F3J2[0]
    gsF1 = F1J1[0] + F2J2[1] + F3J2[1]

    gfF2 = F1J2[0] + F2J1[1] + F3J2[1]
    gsF2 = F1J2[1] + F2J1[0] + F3J2[0]

    gfF3 = F1J2[1] + F2J2[1] + F3J1[1]
    gsF3 = F1J2[0] + F2J2[0] + F3J1[0]

    tabelaGF = [[GF[0]['País'], PF0, gfF0, gsF0, gfF0 - gsF0],
                [GF[1]['País'], PF1, gfF1, gsF1, gfF1 - gsF1],
                [GF[2]['País'], PF2, gfF2, gsF2, gfF2 - gsF2],
                [GF[3]['País'], PF3, gfF3, gsF3, gfF3 - gsF3]]

    print('\n----GRUPO F----\n ')
    print('País    / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(tabelaGF[0], tabelaGF[1],
          tabelaGF[2], tabelaGF[3]))

    # _______________ FIM DO GRUPO F_______________________
    # ___________________GRUPO G___________________
    # Grupo G, rodada 1:
    print('\n JOGOS - GRUPO G \n')

    print('\n RODADA 1: \n')
    G1J1 = resultado(int(GG[0]['Nível']), int(GG[1]['Nível']))  # chamando (f)

    print('{} {} x {} {}'.format(GG[0]['País'],
          G1J1[0], G1J1[1], GG[1]['País']))

    # Estrutura de pontuação da partida:
    if G1J1[0] > G1J1[1]:
        PG0 = PG0 + 3
    elif G1J1[0] < G1J1[1]:
        PG1 = PG1 + 3
    else:
        PG0 = PG0 + 1
        PG1 = PG1 + 1
    # FIM DO JOGO 1
    G1J2 = resultado(int(GG[2]['Nível']), int(GG[3]['Nível']))

    print('{} {} x {} {}'.format(GG[2]['País'],
          G1J2[0], G1J2[1], GG[3]['País']))

    # Estrutura de pontuação da partida:
    if G1J2[0] > G1J2[1]:
        PG2 = PG2 + 3
    elif G1J2[0] < G1J2[1]:
        PG3 = PG3 + 3
    else:
        PG2 = PG2 + 1
        PG3 = PG3 + 1
    # FIM DO JOGO 2

    # Grupo G, rodada 2:
    print('\n RODADA 2: \n')
    G2J1 = resultado(int(GG[0]['Nível']), int(GG[2]['Nível']))

    print('{} {} x {} {}'.format(GG[0]['País'],
          G2J1[0], G2J1[1], GG[2]['País']))

    # Estrutura de pontuação da partida:
    if G2J1[0] > G2J1[1]:
        PG0 = PG0 + 3
    elif G2J1[0] < G2J1[1]:
        PG2 = PG2 + 3
    else:
        PG0 = PG0 + 1
        PG2 = PG2 + 1
    # FIM DO JOGO 1

    G2J2 = resultado(int(GG[1]['Nível']), int(GG[3]['Nível']))

    print('{} {} x {} {}'.format(GG[1]['País'],
          G2J2[0], G2J2[1], GG[3]['País']))

    # Estrutura de pontuação da partida:
    if G2J2[0] > G2J2[1]:
        PG1 = PG1 + 3
    elif G2J2[0] < G2J2[1]:
        PG3 = PG3 + 3
    else:
        PG1 = PG1 + 1
        PG3 = PG3 + 1
    # FIM DO JOGO 2

    # Grupo G, rodada 3:
    print('\n RODADA 3: \n')
    G3J1 = resultado(int(GG[0]['Nível']), int(GG[3]['Nível']))

    print('{} {} x {} {}'.format(GG[0]['País'],
          G3J1[0], G3J1[1], GG[3]['País']))

    # Estrutura de pontuação da partida:
    if G3J1[0] > G3J1[1]:
        PG0 = PG0 + 3
    elif G3J1[0] < G3J1[1]:
        PG3 = PG3 + 3
    else:
        PG0 = PG0 + 1
        PG3 = PG3 + 1
    # FIM DO JOGO 1

    G3J2 = resultado(int(GG[1]['Nível']), int(GG[2]['Nível']))

    print('{} {} x {} {}'.format(GG[1]['País'],
          G3J2[0], G3J2[1], GG[2]['País']))

    # Estrutura de pontuação da partida:
    if G3J2[0] > G3J2[1]:
        PG1 = PG1 + 3
    elif G3J2[0] < G3J2[1]:
        PG2 = PG2 + 3
    else:
        PG1 = PG1 + 1
        PG2 = PG2 + 1
    # FIM DO JOGO 2
    # SALDOS:
    gfG0 = G1J1[0] + G2J1[0] + G3J1[0]
    gsG0 = G1J1[1] + G2J1[1] + G3J1[1]

    gfG1 = G1J1[1] + G2J2[0] + G3J2[0]
    gsG1 = G1J1[0] + G2J2[1] + G3J2[1]

    gfG2 = G1J2[0] + G2J1[1] + G3J2[1]
    gsG2 = G1J2[1] + G2J1[0] + G3J2[0]

    gfG3 = G1J2[1] + G2J2[1] + G3J1[1]
    gsG3 = G1J2[0] + G2J2[0] + G3J1[0]

    tabelaGG = [[GG[0]['País'], PG0, gfG0, gsG0, gfG0 - gsG0],
                [GG[1]['País'], PG1, gfG1, gsG1, gfG1 - gsG1],
                [GG[2]['País'], PG2, gfG2, gsG2, gfG2 - gsG2],
                [GG[3]['País'], PG3, gfG3, gsG3, gfG3 - gsG3]]

    print('\n----GRUPO G----\n ')
    print('País    / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(tabelaGG[0], tabelaGG[1],
          tabelaGG[2], tabelaGG[3]))

    # _______________ FIM DO GRUPO G_______________________
    # ___________________GRUPO H___________________
    # Grupo H, rodada 1:
    print('\n JOGOS - GRUPO H \n')

    print('\n RODADA 1: \n')
    H1J1 = resultado(int(GH[0]['Nível']), int(GH[1]['Nível']))  # chamando (f)

    print('{} {} x {} {}'.format(GH[0]['País'],
          H1J1[0], H1J1[1], GH[1]['País']))

    # Estrutura de pontuação da partida:
    if H1J1[0] > H1J1[1]:
        PH0 = PH0 + 3
    elif H1J1[0] < H1J1[1]:
        PH1 = PH1 + 3
    else:
        PH0 = PH0 + 1
        PH1 = PH1 + 1
    # FIM DO JOGO 1
    H1J2 = resultado(int(GH[2]['Nível']), int(GH[3]['Nível']))

    print('{} {} x {} {}'.format(GH[2]['País'],
          H1J2[0], H1J2[1], GH[3]['País']))

    # Estrutura de pontuação da partida:
    if H1J2[0] > H1J2[1]:
        PH2 = PH2 + 3
    elif H1J2[0] < H1J2[1]:
        PH3 = PH3 + 3
    else:
        PH2 = PH2 + 1
        PH3 = PH3 + 1
    # FIM DO JOGO 2

    # Grupo H, rodada 2:
    print('\n RODADA 2: \n')
    H2J1 = resultado(int(GH[0]['Nível']), int(GH[2]['Nível']))

    print('{} {} x {} {}'.format(GH[0]['País'],
          H2J1[0], H2J1[1], GH[2]['País']))

    # Estrutura de pontuação da partida:
    if H2J1[0] > H2J1[1]:
        PH0 = PH0 + 3
    elif H2J1[0] < H2J1[1]:
        PH2 = PH2 + 3
    else:
        PH0 = PH0 + 1
        PH2 = PH2 + 1
    # FIM DO JOGO 1

    H2J2 = resultado(int(GH[1]['Nível']), int(GH[3]['Nível']))

    print('{} {} x {} {}'.format(GH[1]['País'],
          H2J2[0], H2J2[1], GH[3]['País']))

    # Estrutura de pontuação da partida:
    if H2J2[0] > H2J2[1]:
        PH1 = PH1 + 3
    elif H2J2[0] < H2J2[1]:
        PH3 = PH3 + 3
    else:
        PH1 = PH1 + 1
        PH3 = PH3 + 1
    # FIM DO JOGO 2

    # Grupo H, rodada 3:
    print('\n RODADA 3: \n')
    H3J1 = resultado(int(GH[0]['Nível']), int(GH[3]['Nível']))

    print('{} {} x {} {}'.format(GH[0]['País'],
          H3J1[0], H3J1[1], GH[3]['País']))

    # Estrutura de pontuação da partida:
    if H3J1[0] > H3J1[1]:
        PH0 = PH0 + 3
    elif H3J1[0] < H3J1[1]:
        PH3 = PH3 + 3
    else:
        PH0 = PH0 + 1
        PH3 = PH3 + 1
    # FIM DO JOGO 1

    H3J2 = resultado(int(GH[1]['Nível']), int(GH[2]['Nível']))

    print('{} {} x {} {}'.format(GH[1]['País'],
          H3J2[0], H3J2[1], GH[2]['País']))

    # Estrutura de pontuação da partida:
    if H3J2[0] > H3J2[1]:
        PH1 = PH1 + 3
    elif H3J2[0] < H3J2[1]:
        PH2 = PH2 + 3
    else:
        PH1 = PH1 + 1
        PH2 = PH2 + 1
    # FIM DO JOGO 2
    # SALDOS:
    gfH0 = H1J1[0] + H2J1[0] + H3J1[0]
    gsH0 = H1J1[1] + H2J1[1] + H3J1[1]

    gfH1 = H1J1[1] + H2J2[0] + H3J2[0]
    gsH1 = H1J1[0] + H2J2[1] + H3J2[1]

    gfH2 = H1J2[0] + H2J1[1] + H3J2[1]
    gsH2 = H1J2[1] + H2J1[0] + H3J2[0]

    gfH3 = H1J2[1] + H2J2[1] + H3J1[1]
    gsH3 = H1J2[0] + H2J2[0] + H3J1[0]

    tabelaGH = [[GH[0]['País'], PH0, gfH0, gsH0, gfH0 - gsH0],
                [GH[1]['País'], PH1, gfH1, gsH1, gfH1 - gsH1],
                [GH[2]['País'], PH2, gfH2, gsH2, gfH2 - gsH2],
                [GH[3]['País'], PH3, gfH3, gsH3, gfH3 - gsH3]]

    print('\n----GRUPO H----\n ')
    print('País    / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(tabelaGH[0], tabelaGH[1],
          tabelaGH[2], tabelaGH[3]))

    # _______________ FIM DO GRUPO H_______________________
    return [GA, GB, GC, GD, GE, GF, GG, GH, tabelaGA, tabelaGB,
            tabelaGC, tabelaGD, tabelaGE, tabelaGF, tabelaGG, tabelaGH]
