# Código por Gustavo Albuquerque - 20/04/2021
from v2_simulador_grupos import tabela_grupos
from sorteio import sorteio_copa
from v2p2_partida import resultado
from penaltis import desempate


def copa_mundo(grupos, RA, RB, RC, RD, RE, RF, RG, RH):
    # os grupos em si, com as forças atreladas ao time
    timesA = grupos[0]
    timesB = grupos[1]
    timesC = grupos[2]
    timesD = grupos[3]
    timesE = grupos[4]
    timesF = grupos[5]
    timesG = grupos[6]
    timesH = grupos[7]
    # tabela dos grupos
    classif_A = RA[0]
    classif_B = RB[0]
    classif_C = RC[0]
    classif_D = RD[0]
    classif_E = RE[0]
    classif_F = RF[0]
    classif_G = RG[0]
    classif_H = RH[0]

    # esvaziando string penaltis dos duelos
    TO1P = " "
    TO2P = " "
    TO3P = " "
    TO4P = " "
    TO5P = " "
    TO6P = " "
    TO7P = " "
    TO8P = " "
    TQ1P = " "
    TQ2P = " "
    TQ3P = " "
    TQ4P = " "
    TSF1P = " "
    TSF2P = " "
    TTLP = " "
    TFINALP = " "

    # MONTANDO OS CLASSIFICADOS E OS NÍVEIS

    for time in timesA:
        if time['País'] == classif_A[0][0]:
            A1 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesA:
        if time['País'] == classif_A[1][0]:
            A2 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesB:
        if time['País'] == classif_B[0][0]:
            B1 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesB:
        if time['País'] == classif_B[1][0]:
            B2 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesC:
        if time['País'] == classif_C[0][0]:
            C1 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesC:
        if time['País'] == classif_C[1][0]:
            C2 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesD:
        if time['País'] == classif_D[0][0]:
            D1 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesD:
        if time['País'] == classif_D[1][0]:
            D2 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesE:
        if time['País'] == classif_E[0][0]:
            E1 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesE:
        if time['País'] == classif_E[1][0]:
            E2 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesF:
        if time['País'] == classif_F[0][0]:
            F1 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesF:
        if time['País'] == classif_F[1][0]:
            F2 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesG:
        if time['País'] == classif_G[0][0]:
            G1 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesG:
        if time['País'] == classif_G[1][0]:
            G2 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesH:
        if time['País'] == classif_H[0][0]:
            H1 = [time['País'], time['Nível'], time['Jogadores']]

    for time in timesH:
        if time['País'] == classif_H[1][0]:
            H2 = [time['País'], time['Nível'], time['Jogadores']]

    # Jogo O1

    O1 = resultado(int(A1[1]), int(B2[1]), A1[2], B2[2], pro=True, dec=True)
    pO1 = O1

    TO1 = ('\n{} {} x {} {}\n'.format(A1[0],
                                      O1[0], O1[1], B2[0]))

    # Estrutura de classificação:
    if O1[0] > O1[1]:
        QF1_1 = A1
    elif O1[0] < O1[1]:
        QF1_1 = B2
    else:
        O1 = desempate()
        TO1P = ('Penaltis: \n{} {} x {} {}\n'.format(A1[0],
                                                     O1[0], O1[1], B2[0]))
        if O1[0] > O1[1]:
            QF1_1 = A1
        else:
            QF1_1 = B2
    # Fim do jogo O1

    # Jogo O2

    O2 = resultado(int(C1[1]), int(D2[1]), C1[2], D2[2], pro=True, dec=True)
    pO2 = O2

    TO2 = ('\n{} {} x {} {}\n'.format(C1[0],
                                      O2[0], O2[1], D2[0]))

    # Estrutura de classificação:
    if O2[0] > O2[1]:
        QF1_2 = C1
    elif O2[0] < O2[1]:
        QF1_2 = D2
    else:
        O2 = desempate()
        TO2P = ('Penaltis: \n{} {} x {} {}\n'.format(C1[0],
                                                     O2[0], O2[1], D2[0]))
        if O2[0] > O2[1]:
            QF1_2 = C1
        else:
            QF1_2 = D2
    # Fim do jogo O2

    # Jogo O3
    O3 = resultado(int(E1[1]), int(F2[1]), E1[2], F2[2], pro=True, dec=True)
    pO3 = O3

    TO3 = ('\n{} {} x {} {}\n'.format(E1[0],
                                      O3[0], O3[1], F2[0]))

    # Estrutura de classificação:
    if O3[0] > O3[1]:
        QF2_1 = E1
    elif O3[0] < O3[1]:
        QF2_1 = F2
    else:
        O3 = desempate()
        TO3P = ('Penaltis: \n{} {} x {} {}\n'.format(E1[0],
                                                     O3[0], O3[1], F2[0]))
        if O3[0] > O3[1]:
            QF2_1 = E1
        else:
            QF2_1 = F2
    # Fim do jogo O3

    # Jogo O4

    O4 = resultado(int(G1[1]), int(H2[1]), G1[2], H2[2], pro=True, dec=True)
    pO4 = O4

    TO4 = ('\n{} {} x {} {}\n'.format(G1[0],
                                      O4[0], O4[1], H2[0]))

    # Estrutura de classificação:
    if O4[0] > O4[1]:
        QF2_2 = G1
    elif O4[0] < O4[1]:
        QF2_2 = H2
    else:
        O4 = desempate()
        TO4P = ('Penaltis: \n{} {} x {} {}\n'.format(G1[0],
                                                     O4[0], O4[1], H2[0]))
        if O4[0] > O4[1]:
            QF2_2 = G1
        else:
            QF2_2 = H2
    # Fim do jogo O4

    # Jogo O5

    O5 = resultado(int(B1[1]), int(A2[1]), B1[2], A2[2], pro=True, dec=True)
    pO5 = O5

    TO5 = ('\n{} {} x {} {}\n'.format(B1[0],
                                      O5[0], O5[1], A2[0]))

    # Estrutura de classificação:
    if O5[0] > O5[1]:
        QF3_1 = B1
    elif O5[0] < O5[1]:
        QF3_1 = A2
    else:
        O5 = desempate()
        TO5P = ('Penaltis: \n{} {} x {} {}\n'.format(B1[0],
                                                     O5[0], O5[1], A2[0]))
        if O5[0] > O5[1]:
            QF3_1 = B1
        else:
            QF3_1 = A2
    # Fim do jogo O5

    # Jogo O6

    O6 = resultado(int(D1[1]), int(C2[1]), D1[2], C2[2], pro=True, dec=True)
    pO6 = O6

    TO6 = ('\n{} {} x {} {}\n'.format(D1[0],
                                      O6[0], O6[1], C2[0]))

    # Estrutura de classificação:
    if O6[0] > O6[1]:
        QF3_2 = D1
    elif O6[0] < O6[1]:
        QF3_2 = C2
    else:
        O6 = desempate()
        TO6P = ('Penaltis: \n{} {} x {} {}\n'.format(D1[0],
                                                     O6[0], O6[1], C2[0]))
        if O6[0] > O6[1]:
            QF3_2 = D1
        else:
            QF3_2 = C2
    # Fim do jogo O6

    # Jogo O7

    O7 = resultado(int(F1[1]), int(E2[1]), F1[2], E2[2], pro=True, dec=True)
    pO7 = O7

    TO7 = ('\n{} {} x {} {}\n'.format(F1[0],
                                      O7[0], O7[1], E2[0]))

    # Estrutura de classificação:
    if O7[0] > O7[1]:
        QF4_1 = F1
    elif O7[0] < O7[1]:
        QF4_1 = E2
    else:
        O7 = desempate()
        TO7P = ('Penaltis: \n{} {} x {} {}\n'.format(F1[0],
                                                     O7[0], O7[1], E2[0]))
        if O7[0] > O7[1]:
            QF4_1 = F1
        else:
            QF4_1 = E2

    # Fim do jogo O7

    # Jogo O8
    O8 = resultado(int(H1[1]), int(G2[1]), H1[2], G2[2], pro=True, dec=True)
    pO8 = O8

    TO8 = ('\n{} {} x {} {}\n'.format(H1[0],
                                      O8[0], O8[1], G2[0]))

    # Estrutura de classificação:
    if O8[0] > O8[1]:
        QF4_2 = H1
    elif O8[0] < O8[1]:
        QF4_2 = G2
    else:
        O8 = desempate()
        TO8P = ('Penaltis: \n{} {} x {} {}\n'.format(H1[0],
                                                     O8[0], O8[1], G2[0]))
        if O8[0] > O8[1]:
            QF4_2 = H1
        else:
            QF4_2 = G2
    # Fim do jogo O8

    # QUARTAS DE FINAL:

    # Jogo QF1

    QF1 = resultado(int(QF1_1[1]), int(QF1_2[1]), QF1_1[2], QF1_2[2], pro=True,
                    dec=True)
    pQF1 = QF1

    TQ1 = ('\n{} {} x {} {}\n'.format(QF1_1[0],
                                      QF1[0], QF1[1], QF1_2[0]))

    # Estrutura de classificação:
    if QF1[0] > QF1[1]:
        SF1_1 = QF1_1
    elif QF1[0] < QF1[1]:
        SF1_1 = QF1_2
    else:
        QF1 = desempate()
        TQ1P = ('Penaltis: \n{} {} x {} {}\n'.format(QF1_1[0],
                                                     QF1[0], QF1[1], QF1_2[0]))
        if QF1[0] > QF1[1]:
            SF1_1 = QF1_1
        else:
            SF1_1 = QF1_2

    # Fim do jogo QF1

    # Jogo QF2

    QF2 = resultado(int(QF2_1[1]), int(QF2_2[1]), QF2_1[2], QF2_2[2], pro=True,
                    dec=True)
    pQF2 = QF2

    TQ2 = ('\n{} {} x {} {}\n'.format(QF2_1[0],
                                      QF2[0], QF2[1], QF2_2[0]))

    # Estrutura de classificação:
    if QF2[0] > QF2[1]:
        SF1_2 = QF2_1
    elif QF2[0] < QF2[1]:
        SF1_2 = QF2_2
    else:
        QF2 = desempate()
        TQ2P = ('Penaltis: \n{} {} x {} {}\n'.format(QF2_1[0],
                                                     QF2[0], QF2[1], QF2_2[0]))
        if QF2[0] > QF2[1]:
            SF1_2 = QF2_1
        else:
            SF1_2 = QF2_2
    # Fim do jogo QF2

    # Jogo QF3

    QF3 = resultado(int(QF3_1[1]), int(QF3_2[1]), QF3_1[2], QF3_2[2], pro=True,
                    dec=True)
    pQF3 = QF3

    TQ3 = ('\n{} {} x {} {}\n'.format(QF3_1[0],
                                      QF3[0], QF3[1], QF3_2[0]))

    # Estrutura de classificação:
    if QF3[0] > QF3[1]:
        SF2_1 = QF3_1
    elif QF3[0] < QF3[1]:
        SF2_1 = QF3_2
    else:
        QF3 = desempate()
        TQ3P = ('Penaltis: \n{} {} x {} {}\n'.format(QF3_1[0],
                                                     QF3[0], QF3[1], QF3_2[0]))
        if QF3[0] > QF3[1]:
            SF2_1 = QF3_1
        else:
            SF2_1 = QF3_2
    # Fim do jogo QF3

    # Jogo QF4

    QF4 = resultado(int(QF4_1[1]), int(QF4_2[1]), QF4_1[2], QF4_2[2], pro=True,
                    dec=True)
    pQF4 = QF4

    TQ4 = ('\n{} {} x {} {}\n'.format(QF4_1[0],
                                      QF4[0], QF4[1], QF4_2[0]))

    # Estrutura de classificação:
    if QF4[0] > QF4[1]:
        SF2_2 = QF4_1
    elif QF4[0] < QF4[1]:
        SF2_2 = QF4_2
    else:
        QF4 = desempate()
        TQ4P = ('Penaltis: \n{} {} x {} {}\n'.format(QF4_1[0],
                                                     QF4[0], QF4[1], QF4_2[0]))
        if QF4[0] > QF4[1]:
            SF2_2 = QF4_1
        else:
            SF2_2 = QF4_2
    # Fim do jogo QF4

    # SEMI FINAL
    # Jogo SF1

    SF1 = resultado(int(SF1_1[1]), int(SF1_2[1]), SF1_1[2], SF1_2[2], pro=True,
                    dec=True)
    pSF1 = SF1

    TSF1 = ('\n{} {} x {} {}\n'.format(SF1_1[0],
                                       SF1[0], SF1[1], SF1_2[0]))

    # Estrutura de classificação:
    if SF1[0] > SF1[1]:
        FINAL_1 = SF1_1
        TL1 = SF1_2
    elif SF1[0] < SF1[1]:
        FINAL_1 = SF1_2
        TL1 = SF1_1
    else:
        SF1 = desempate()
        TSF1P = ('Penaltis: \n{} {} x {} {}\n'.format(
            SF1_1[0], SF1[0], SF1[1], SF1_2[0]))
        if SF1[0] > SF1[1]:
            FINAL_1 = SF1_1
            TL1 = SF1_2
        else:
            FINAL_1 = SF1_2
            TL1 = SF1_1
    # Fim do jogo SF1

    # Jogo SF2

    SF2 = resultado(int(SF2_1[1]), int(SF2_2[1]), SF2_1[2], SF2_2[2], pro=True,
                    dec=True)
    pSF2 = SF2

    TSF2 = ('\n{} {} x {} {}\n'.format(SF2_1[0],
                                       SF2[0], SF2[1], SF2_2[0]))

    # Estrutura de classificação:
    if SF2[0] > SF2[1]:
        FINAL_2 = SF2_1
        TL2 = SF2_2
    elif SF2[0] < SF2[1]:
        FINAL_2 = SF2_2
        TL2 = SF2_1
    else:
        SF2 = desempate()
        TSF2P = ('Penaltis: \n{} {} x {} {}\n'.format(
            SF2_1[0], SF2[0], SF2[1], SF2_2[0]))
        if SF2[0] > SF2[1]:
            FINAL_2 = SF2_1
            TL2 = SF2_2
        else:
            FINAL_2 = SF2_2
            TL2 = SF2_1
    # Fim do jogo SF2

    # Jogo TL

    TL = resultado(int(TL1[1]), int(TL2[1]), TL1[2], TL2[2], pro=True,
                   dec=True)
    pTL = TL

    TTL = ('\n{} {} x {} {}\n'.format(TL1[0],
                                      TL[0], TL[1], TL2[0]))

    # Estrutura de classificação:
    if TL[0] > TL[1]:
        Terceiro = TL1
        Quarto = TL2

    elif TL[0] < TL[1]:
        Terceiro = TL2
        Quarto = TL1

    else:
        TL = desempate()
        TTLP = ('Penaltis: \n{} {} x {} {}\n'.format(TL1[0],
                                                     TL[0], TL[1], TL2[0]))
        if TL[0] > TL[1]:
            Terceiro = TL1
            Quarto = TL2

        else:
            Terceiro = TL2
            Quarto = TL1

    # Fim do jogo TL

    # Jogo final

    final = resultado(int(FINAL_1[1]), int(FINAL_2[1]),
                      FINAL_1[2], FINAL_2[2], pro=True, dec=True)
    pfinal = final

    TFINAL = ('\n{} {} x {} {}\n'.format(FINAL_1[0],
                                         final[0], final[1], FINAL_2[0]))

    # Estrutura de classificação:
    if final[0] > final[1]:
        Camp = FINAL_1
        Vice = FINAL_2
    elif final[0] < final[1]:
        Camp = FINAL_2
        Vice = FINAL_1
    else:
        final = desempate()
        TFINALP = ('Penaltis: \n{} {} x {} {}\n'.format(
            FINAL_1[0], final[0], final[1], FINAL_2[0]))
        if final[0] > final[1]:
            Camp = FINAL_1
            Vice = FINAL_2

        else:
            Camp = FINAL_2
            Vice = FINAL_1

    # Fim do Mata Mata

    mm_mins = [pO1[2], pO1[3], pO2[2], pO2[3],
               pO3[2], pO3[3], pO4[2], pO4[3],
               pO5[2], pO5[3], pO6[2], pO6[3],
               pO7[2], pO7[3], pO8[2], pO8[3],
               pQF1[2], pQF1[3], pQF2[2], pQF2[3],
               pQF3[2], pQF3[3], pQF4[2], pQF4[3],
               pSF1[2], pSF1[3], pSF2[2], pSF2[3],
               pTL[2], pTL[3], pfinal[2], pfinal[3]]

    return (TO1, TO2, TO3, TO4, TO5, TO6, TO7, TO8,
            TO1P, TO2P, TO3P, TO4P, TO5P, TO6P, TO7P, TO8P,
            TQ1, TQ2, TQ3, TQ4, TSF1, TSF2, TTL, TFINAL,
            TQ1P, TQ2P, TQ3P, TQ4P, TSF1P, TSF2P, TTLP, TFINALP,
            Quarto, Terceiro, Vice, Camp, mm_mins)


def textos_matamata(oi1, oi2, oi3, oi4, oi5, oi6, oi7, oi8,
                    oi1p, oi2p, oi3p, oi4p, oi5p, oi6p, oi7p, oi8p,
                    ql1, ql2, ql3, ql4, se1, se2, ter, fin,
                    ql1p, ql2p, ql3p, ql4p, se1p, se2p, terp, finp,
                    quart, terce, vice, camp, m):

    texto_oi1 = f"""
    {oi1}
    {oi1p}
    Gols: {m[0]} (X) {m[1]}
    _____________________________________________________
    {oi2}
    {oi2p}
    Gols: {m[2]} (X) {m[3]}
    _____________________________________________________
    """
    texto_oi2 = f"""
    {oi3}
    {oi3p}
    Gols: {m[4]} (X) {m[5]}
    _____________________________________________________
    {oi4}
    {oi4p}
    Gols: {m[6]} (X) {m[7]}
    _____________________________________________________
    """
    texto_oi3 = f"""
    {oi5}
    {oi5p}
    Gols: {m[8]} (X) {m[9]}
    _____________________________________________________
    {oi6}
    {oi6p}
    Gols: {m[10]} (X) {m[11]}
    _____________________________________________________
    """
    texto_oi4 = f"""
    {oi7}
    {oi7p}
    Gols: {m[12]} (X) {m[13]}
    _____________________________________________________
    {oi8}
    {oi8p}
    Gols: {m[14]} (X) {m[15]}
    _____________________________________________________
    """
    texto_qua1 = f"""
    {ql1}
    {ql1p}
    Gols: {m[16]} (X) {m[17]}
    _____________________________________________________
    {ql2}
    {ql2p}
    Gols: {m[18]} (X) {m[19]}
    _____________________________________________________
    """
    texto_qua2 = f"""
    {ql3}
    {ql3p}
    Gols: {m[20]} (X) {m[21]}
    _____________________________________________________
    {ql4}
    {ql4p}
    Gols: {m[22]} (X) {m[23]}
    _____________________________________________________
    """
    texto_semi = f"""
    {se1}
    {se1p}
    Gols: {m[24]} (X) {m[25]}
    _____________________________________________________
    {se2}
    {se2p}
    Gols: {m[26]} (X) {m[27]}
    _____________________________________________________
    """
    texto_tl = f"""
    {ter}
    {terp}
    Gols: {m[28]} (X) {m[29]}
    _____________________________________________________
    """
    texto_final = f"""
    {fin}
    {finp}
    Gols: {m[30]} (X) {m[31]}

    _______________________________________
    {camp[0]} foi a seleção campeã!
    {vice[0]} foi a seleção vice-campeã
    {terce[0]} ficou em terceiro
    {quart[0]} ficou em quarto
    """

    return [texto_oi1, texto_oi2, texto_oi3, texto_oi4,
            texto_qua1, texto_qua2, texto_semi, texto_tl, texto_final]


if __name__ == '__main__':
    grupinhos = sorteio_copa()
    RG1 = tabela_grupos(grupinhos[0])
    RG2 = tabela_grupos(grupinhos[1])
    RG3 = tabela_grupos(grupinhos[2])
    RG4 = tabela_grupos(grupinhos[3])
    RG5 = tabela_grupos(grupinhos[4])
    RG6 = tabela_grupos(grupinhos[5])
    RG7 = tabela_grupos(grupinhos[6])
    RG8 = tabela_grupos(grupinhos[7])
    copa = copa_mundo(grupinhos, RG1, RG2, RG3, RG4, RG5, RG6, RG7, RG8)
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = textos_matamata(*copa)
