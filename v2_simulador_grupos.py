from v2p2_partida import resultado
import operator


def tabela_grupos(grupo):
    PA0, PA1, PA2, PA3 = 0, 0, 0, 0

    A1J1 = resultado(int(grupo[0]['Nível']), int(grupo[1]['Nível']),
                     (grupo[0]['Jogadores']), (grupo[1]['Jogadores']))

    # Estrutura de pontuação da partida:
    if A1J1[0] > A1J1[1]:
        PA0 = PA0 + 3
    elif A1J1[0] < A1J1[1]:
        PA1 = PA1 + 3
    else:
        PA0 = PA0 + 1
        PA1 = PA1 + 1
    # FIM DO JOGO 1
    A1J2 = resultado(int(grupo[2]['Nível']), int(grupo[3]['Nível']),
                     (grupo[2]['Jogadores']), (grupo[3]['Jogadores']))

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

    A2J1 = resultado(int(grupo[0]['Nível']), int(grupo[2]['Nível']),
                     (grupo[0]['Jogadores']), (grupo[2]['Jogadores']))

    # Estrutura de pontuação da partida:
    if A2J1[0] > A2J1[1]:
        PA0 = PA0 + 3
    elif A2J1[0] < A2J1[1]:
        PA2 = PA2 + 3
    else:
        PA0 = PA0 + 1
        PA2 = PA2 + 1
    # FIM DO JOGO 1

    A2J2 = resultado(int(grupo[1]['Nível']), int(grupo[3]['Nível']),
                     (grupo[1]['Jogadores']), (grupo[3]['Jogadores']))
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
    A3J1 = resultado(int(grupo[0]['Nível']), int(grupo[3]['Nível']),
                     (grupo[0]['Jogadores']), (grupo[3]['Jogadores']))

    # Estrutura de pontuação da partida:
    if A3J1[0] > A3J1[1]:
        PA0 = PA0 + 3
    elif A3J1[0] < A3J1[1]:
        PA3 = PA3 + 3
    else:
        PA0 = PA0 + 1
        PA3 = PA3 + 1
    # FIM DO JOGO 1

    A3J2 = resultado(int(grupo[1]['Nível']), int(grupo[2]['Nível']),
                     (grupo[1]['Jogadores']), (grupo[2]['Jogadores']))
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

    tabelagrupo = [[grupo[0]['País'], PA0, gfA0, gsA0, gfA0 - gsA0],
                   [grupo[1]['País'], PA1, gfA1, gsA1, gfA1 - gsA1],
                   [grupo[2]['País'], PA2, gfA2, gsA2, gfA2 - gsA2],
                   [grupo[3]['País'], PA3, gfA3, gsA3, gfA3 - gsA3]]

    ordenacao = sorted(tabelagrupo, key=operator.itemgetter(1, 4, 2))
    classificacao = [ordenacao[3], ordenacao[2], ordenacao[1], ordenacao[0]]
    jogos = {
        'R1': [
            [grupo[0]['País'], A1J1[0], A1J1[1], grupo[1]['País']],
            [grupo[2]['País'], A1J2[0], A1J2[1], grupo[3]['País']]
        ],
        'R2': [
            [grupo[0]['País'], A2J1[0], A2J1[1], grupo[2]['País']],
            [grupo[1]['País'], A2J2[0], A2J2[1], grupo[3]['País']],
        ],
        'R3': [
            [grupo[0]['País'], A3J1[0], A3J1[1], grupo[3]['País']],
            [grupo[1]['País'], A3J2[0], A3J2[1], grupo[2]['País']],
        ]
    }
    minutagens_grupos = [A1J1[2], A1J1[3], A1J2[2], A1J2[3],
                         A2J1[2], A2J1[3], A2J2[2], A2J2[3],
                         A3J1[2], A3J1[3], A3J2[2], A3J2[3]]
    return [classificacao, jogos, minutagens_grupos]


def textos_grupo(cla, j, m):

    pa, pb, pc, pd = cla[0][0], cla[1][0], cla[2][0], cla[3][0]
    pta, ptb, ptc, ptd = cla[0][1], cla[1][1], cla[2][1], cla[3][1]
    gfa, gfb, gfc, gfd = cla[0][2], cla[1][2], cla[2][2], cla[3][2]
    gsa, gsb, gsc, gsd = cla[0][3], cla[1][3], cla[2][3], cla[3][3]
    sga, sgb, sgc, sgd = cla[0][4], cla[1][4], cla[2][4], cla[3][4]

    tabela = [
            [pa, pta, gfa, gsa, sga],
            [pb, ptb, gfb, gsb, sgb],
            [pc, ptc, gfc, gsc, sgc],
            [pd, ptd, gfd, gsd, sgd],
            ]

    texto_classif = tabela
    texto_1rod = f"""
    \nPRIMEIRA RODADA:\n
    {j['R1'][0][0]} {j['R1'][0][1]} x {j['R1'][0][2]} {j['R1'][0][3]}\n
    Gols:
    {j['R1'][0][0][0:3].upper()}: {m[0]}
    {j['R1'][0][3][0:3].upper()}: {m[1]}\n
    {j['R1'][1][0]} {j['R1'][1][1]} x {j['R1'][1][2]} {j['R1'][1][3]}\n
    Gols:
    {j['R1'][1][0][0:3].upper()}: {m[2]}
    {j['R1'][1][3][0:3].upper()}: {m[3]}
    """
    texto_2rod = f"""
    \nSEGUNDA RODADA:\n
    {j['R2'][0][0]} {j['R2'][0][1]} x {j['R2'][0][2]} {j['R2'][0][3]}\n
    Gols:
    {j['R2'][0][0][0:3].upper()}: {m[4]}
    {j['R2'][0][3][0:3].upper()}: {m[5]}\n
    {j['R2'][1][0]} {j['R2'][1][1]} x {j['R2'][1][2]} {j['R2'][1][3]}\n
    Gols:
    {j['R2'][1][0][0:3].upper()}: {m[6]}
    {j['R2'][1][3][0:3].upper()}: {m[7]}
    """
    texto_3rod = f"""
    \nTERCEIRA RODADA:\n
    {j['R3'][0][0]} {j['R3'][0][1]} x {j['R3'][0][2]} {j['R3'][0][3]}\n
    Gols:
    {j['R3'][0][0][0:3].upper()}: {m[8]}
    {j['R3'][0][3][0:3].upper()}: {m[9]}\n
    {j['R3'][1][0]} {j['R3'][1][1]} x {j['R3'][1][2]} {j['R3'][1][3]}\n
    Gols:
    {j['R3'][1][0][0:3].upper()}: {m[10]}
    {j['R3'][1][3][0:3].upper()}: {m[11]}
    """
    return [texto_classif, texto_1rod, texto_2rod, texto_3rod]
