from placar import resultado
import operator


def tabela_grupos(grupo):
    PA0, PA1, PA2, PA3 = 0, 0, 0, 0

    A1J1 = resultado(int(grupo[0]['Nível']), int(grupo[1]['Nível']))

    # Estrutura de pontuação da partida:
    if A1J1[0] > A1J1[1]:
        PA0 = PA0 + 3
    elif A1J1[0] < A1J1[1]:
        PA1 = PA1 + 3
    else:
        PA0 = PA0 + 1
        PA1 = PA1 + 1
    # FIM DO JOGO 1
    A1J2 = resultado(int(grupo[2]['Nível']), int(grupo[3]['Nível']))

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

    A2J1 = resultado(int(grupo[0]['Nível']), int(grupo[2]['Nível']))

    # Estrutura de pontuação da partida:
    if A2J1[0] > A2J1[1]:
        PA0 = PA0 + 3
    elif A2J1[0] < A2J1[1]:
        PA2 = PA2 + 3
    else:
        PA0 = PA0 + 1
        PA2 = PA2 + 1
    # FIM DO JOGO 1

    A2J2 = resultado(int(grupo[1]['Nível']), int(grupo[3]['Nível']))

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
    A3J1 = resultado(int(grupo[0]['Nível']), int(grupo[3]['Nível']))

    # Estrutura de pontuação da partida:
    if A3J1[0] > A3J1[1]:
        PA0 = PA0 + 3
    elif A3J1[0] < A3J1[1]:
        PA3 = PA3 + 3
    else:
        PA0 = PA0 + 1
        PA3 = PA3 + 1
    # FIM DO JOGO 1

    A3J2 = resultado(int(grupo[1]['Nível']), int(grupo[2]['Nível']))

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
    return [classificacao, jogos]


def textos_grupo(classif, j):
    texto_classif = f"""
    CLASSIFICAÇÃO:
    País        / Pontos / GF / GS / SG
    {classif[0]}
    {classif[1]}
    {classif[2]}
    {classif[3]}
    """
    texto_1rod = f"""
    \nPRIMEIRA RODADA:\n
    {j['R1'][0][0]} {j['R1'][0][1]} x {j['R1'][0][2]} {j['R1'][0][3]}\n
    {j['R1'][1][0]} {j['R1'][1][1]} x {j['R1'][1][2]} {j['R1'][1][3]}\n
    """
    texto_2rod = f"""
    \nSEGUNDA RODADA:\n
    {j['R2'][0][0]} {j['R2'][0][1]} x {j['R2'][0][2]} {j['R2'][0][3]}\n
    {j['R2'][1][0]} {j['R2'][1][1]} x {j['R2'][1][2]} {j['R2'][1][3]}\n
    """
    texto_3rod = f"""
    \nTERCEIRA RODADA:\n
    {j['R3'][0][0]} {j['R3'][0][1]} x {j['R3'][0][2]} {j['R3'][0][3]}\n
    {j['R3'][1][0]} {j['R3'][1][1]} x {j['R3'][1][2]} {j['R3'][1][3]}\n
    """
    return [texto_classif, texto_1rod, texto_2rod, texto_3rod]
