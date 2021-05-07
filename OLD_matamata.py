# Código por Gustavo Albuquerque - 20/04/2021
from jogos_grupos import fase_grupos
from placar import resultado
from penaltis import desempate
import operator


def copa_mundo():
    retorno = fase_grupos()
    timesA = retorno[0]
    timesB = retorno[1]
    timesC = retorno[2]
    timesD = retorno[3]
    timesE = retorno[4]
    timesF = retorno[5]
    timesG = retorno[6]
    timesH = retorno[7]
    tabelaA = retorno[8]
    tabelaB = retorno[9]
    tabelaC = retorno[10]
    tabelaD = retorno[11]
    tabelaE = retorno[12]
    tabelaF = retorno[13]
    tabelaG = retorno[14]
    tabelaH = retorno[15]

    classif_A = sorted(tabelaA, key=operator.itemgetter(1, 4, 2))
    classif_B = sorted(tabelaB, key=operator.itemgetter(1, 4, 2))
    classif_C = sorted(tabelaC, key=operator.itemgetter(1, 4, 2))
    classif_D = sorted(tabelaD, key=operator.itemgetter(1, 4, 2))
    classif_E = sorted(tabelaE, key=operator.itemgetter(1, 4, 2))
    classif_F = sorted(tabelaF, key=operator.itemgetter(1, 4, 2))
    classif_G = sorted(tabelaG, key=operator.itemgetter(1, 4, 2))
    classif_H = sorted(tabelaH, key=operator.itemgetter(1, 4, 2))
    # o "key" indica o que a funcao sorted vai usar para sortir a lista!
    print('___________________________________________')
    print('\n________GRUPOS POR CLASSIFICAÇÃO___________\n')
    print('\nGRUPO A:\n')
    print('País      / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(classif_A[3], classif_A[2],
                                    classif_A[1], classif_A[0]))
    print('\nGRUPO B:\n')
    print('País      / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(classif_B[3], classif_B[2],
                                    classif_B[1], classif_B[0]))
    print('\nGRUPO C:\n')
    print('País      / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(classif_C[3], classif_C[2],
                                    classif_C[1], classif_C[0]))
    print('\nGRUPO D:\n')
    print('País      / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(classif_D[3], classif_D[2],
                                    classif_D[1], classif_D[0]))
    print('\nGRUPO E:\n')
    print('País      / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(classif_E[3], classif_E[2],
                                    classif_E[1], classif_E[0]))
    print('\nGRUPO F:\n')
    print('País      / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(classif_F[3], classif_F[2],
                                    classif_F[1], classif_F[0]))
    print('\nGRUPO G:\n')
    print('País      / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(classif_G[3], classif_G[2],
                                    classif_G[1], classif_G[0]))
    print('\nGRUPO H:\n')
    print('País      / Pts / GF / GS / SG')
    print('{}\n{}\n{}\n{}\n'.format(classif_H[3], classif_H[2],
                                    classif_H[1], classif_H[0]))

    # MONTANDO OS CLASSIFICADOS E OS NÍVEIS

    for time in timesA:
        if time['País'] == classif_A[3][0]:
            A1 = [time['País'], time['Nível']]

    for time in timesA:
        if time['País'] == classif_A[2][0]:
            A2 = [time['País'], time['Nível']]

    for time in timesB:
        if time['País'] == classif_B[3][0]:
            B1 = [time['País'], time['Nível']]

    for time in timesB:
        if time['País'] == classif_B[2][0]:
            B2 = [time['País'], time['Nível']]

    for time in timesC:
        if time['País'] == classif_C[3][0]:
            C1 = [time['País'], time['Nível']]

    for time in timesC:
        if time['País'] == classif_C[2][0]:
            C2 = [time['País'], time['Nível']]

    for time in timesD:
        if time['País'] == classif_D[3][0]:
            D1 = [time['País'], time['Nível']]

    for time in timesD:
        if time['País'] == classif_D[2][0]:
            D2 = [time['País'], time['Nível']]

    for time in timesE:
        if time['País'] == classif_E[3][0]:
            E1 = [time['País'], time['Nível']]

    for time in timesE:
        if time['País'] == classif_E[2][0]:
            E2 = [time['País'], time['Nível']]

    for time in timesF:
        if time['País'] == classif_F[3][0]:
            F1 = [time['País'], time['Nível']]

    for time in timesF:
        if time['País'] == classif_F[2][0]:
            F2 = [time['País'], time['Nível']]

    for time in timesG:
        if time['País'] == classif_G[3][0]:
            G1 = [time['País'], time['Nível']]

    for time in timesG:
        if time['País'] == classif_G[2][0]:
            G2 = [time['País'], time['Nível']]

    for time in timesH:
        if time['País'] == classif_H[3][0]:
            H1 = [time['País'], time['Nível']]

    for time in timesH:
        if time['País'] == classif_H[2][0]:
            H2 = [time['País'], time['Nível']]

    print('\n\n_______OITAVAS DE FINAL_______\n\n')

    # Jogo O1
    print('______________________________')

    O1 = resultado(int(A1[1]), int(B2[1]))

    print('\n{} {} x {} {}\n'.format(A1[0],
                                     O1[0], O1[1], B2[0]))

    # Estrutura de classificação:
    if O1[0] > O1[1]:
        QF1_1 = A1
    elif O1[0] < O1[1]:
        QF1_1 = B2
    else:
        print('\nNos penaltis:\n')
        O1 = desempate()
        print('\n{} {} x {} {}\n'.format(A1[0],
                                         O1[0], O1[1], B2[0]))
        if O1[0] > O1[1]:
            QF1_1 = A1
        else:
            QF1_1 = B2
    print('______________________________')
    # Fim do jogo O1

    # Jogo O2
    print('______________________________')

    O2 = resultado(int(C1[1]), int(D2[1]))

    print('\n{} {} x {} {}\n'.format(C1[0],
                                     O2[0], O2[1], D2[0]))

    # Estrutura de classificação:
    if O2[0] > O2[1]:
        QF1_2 = C1
    elif O2[0] < O2[1]:
        QF1_2 = D2
    else:
        print('\nNos penaltis:\n')
        O2 = desempate()
        print('\n{} {} x {} {}\n'.format(C1[0],
                                         O2[0], O2[1], D2[0]))
        if O2[0] > O2[1]:
            QF1_2 = C1
        else:
            QF1_2 = D2
    print('______________________________')
    # Fim do jogo O2

    # Jogo O3
    print('______________________________')

    O3 = resultado(int(E1[1]), int(F2[1]))

    print('\n{} {} x {} {}\n'.format(E1[0],
                                     O3[0], O3[1], F2[0]))

    # Estrutura de classificação:
    if O3[0] > O3[1]:
        QF2_1 = E1
    elif O3[0] < O3[1]:
        QF2_1 = F2
    else:
        print('\nNos penaltis:\n')
        O3 = desempate()
        print('\n{} {} x {} {}\n'.format(E1[0],
                                         O3[0], O3[1], F2[0]))
        if O3[0] > O3[1]:
            QF2_1 = E1
        else:
            QF2_1 = F2
    print('______________________________')
    # Fim do jogo O3

    # Jogo O4
    print('______________________________')

    O4 = resultado(int(G1[1]), int(H2[1]))

    print('\n{} {} x {} {}\n'.format(G1[0],
                                     O4[0], O4[1], H2[0]))

    # Estrutura de classificação:
    if O4[0] > O4[1]:
        QF2_2 = G1
    elif O4[0] < O4[1]:
        QF2_2 = H2
    else:
        print('\nNos penaltis:\n')
        O4 = desempate()
        print('\n{} {} x {} {}\n'.format(G1[0],
                                         O4[0], O4[1], H2[0]))
        if O4[0] > O4[1]:
            QF2_2 = G1
        else:
            QF2_2 = H2
    print('______________________________')
    # Fim do jogo O4

    # Jogo O5
    print('______________________________')

    O5 = resultado(int(B1[1]), int(A2[1]))

    print('\n{} {} x {} {}\n'.format(B1[0],
                                     O5[0], O5[1], A2[0]))

    # Estrutura de classificação:
    if O5[0] > O5[1]:
        QF3_1 = B1
    elif O5[0] < O5[1]:
        QF3_1 = A2
    else:
        print('\nNos penaltis:\n')
        O5 = desempate()
        print('\n{} {} x {} {}\n'.format(B1[0],
                                         O5[0], O5[1], A2[0]))
        if O5[0] > O5[1]:
            QF3_1 = B1
        else:
            QF3_1 = A2
    print('______________________________')
    # Fim do jogo O5

    # Jogo O6
    print('______________________________')

    O6 = resultado(int(D1[1]), int(C2[1]))

    print('\n{} {} x {} {}\n'.format(D1[0],
                                     O6[0], O6[1], C2[0]))

    # Estrutura de classificação:
    if O6[0] > O6[1]:
        QF3_2 = D1
    elif O6[0] < O6[1]:
        QF3_2 = C2
    else:
        print('\nNos penaltis:\n')
        O6 = desempate()
        print('\n{} {} x {} {}\n'.format(D1[0],
                                         O6[0], O6[1], C2[0]))
        if O6[0] > O6[1]:
            QF3_2 = D1
        else:
            QF3_2 = C2
    print('______________________________')
    # Fim do jogo O6

    # Jogo O7
    print('______________________________')

    O7 = resultado(int(F1[1]), int(E2[1]))

    print('\n{} {} x {} {}\n'.format(F1[0],
                                     O7[0], O7[1], E2[0]))

    # Estrutura de classificação:
    if O7[0] > O7[1]:
        QF4_1 = F1
    elif O7[0] < O7[1]:
        QF4_1 = E2
    else:
        print('\nNos penaltis:\n')
        O7 = desempate()
        print('\n{} {} x {} {}\n'.format(F1[0],
                                         O7[0], O7[1], E2[0]))
        if O7[0] > O7[1]:
            QF4_1 = F1
        else:
            QF4_1 = E2
    print('______________________________')
    # Fim do jogo O7

    # Jogo O8
    print('______________________________')

    O8 = resultado(int(H1[1]), int(G2[1]))

    print('\n{} {} x {} {}\n'.format(H1[0],
                                     O8[0], O8[1], G2[0]))

    # Estrutura de classificação:
    if O8[0] > O8[1]:
        QF4_2 = H1
    elif O8[0] < O8[1]:
        QF4_2 = G2
    else:
        print('\nNos penaltis:\n')
        O8 = desempate()
        print('\n{} {} x {} {}\n'.format(H1[0],
                                         O8[0], O8[1], G2[0]))
        if O8[0] > O8[1]:
            QF4_2 = H1
        else:
            QF4_2 = G2
    print('______________________________')
    # Fim do jogo O8

    # QUARTAS DE FINAL:

    print('\n\n_____QUARTAS DE FINAL______\n\n')

    # Jogo QF1
    print('______________________________')

    QF1 = resultado(int(QF1_1[1]), int(QF1_2[1]))

    print('\n{} {} x {} {}\n'.format(QF1_1[0],
                                     QF1[0], QF1[1], QF1_2[0]))

    # Estrutura de classificação:
    if QF1[0] > QF1[1]:
        SF1_1 = QF1_1
    elif QF1[0] < QF1[1]:
        SF1_1 = QF1_2
    else:
        print('\nNos penaltis:\n')
        QF1 = desempate()
        print('\n{} {} x {} {}\n'.format(QF1_1[0],
                                         QF1[0], QF1[1], QF1_2[0]))
        if QF1[0] > QF1[1]:
            SF1_1 = QF1_1
        else:
            SF1_1 = QF1_2
    print('______________________________')
    # Fim do jogo QF1

    # Jogo QF2
    print('______________________________')

    QF2 = resultado(int(QF2_1[1]), int(QF2_2[1]))

    print('\n{} {} x {} {}\n'.format(QF2_1[0],
                                     QF2[0], QF2[1], QF2_2[0]))

    # Estrutura de classificação:
    if QF2[0] > QF2[1]:
        SF1_2 = QF2_1
    elif QF2[0] < QF2[1]:
        SF1_2 = QF2_2
    else:
        print('\nNos penaltis:\n')
        QF2 = desempate()
        print('\n{} {} x {} {}\n'.format(QF2_1[0],
                                         QF2[0], QF2[1], QF2_2[0]))
        if QF2[0] > QF2[1]:
            SF1_2 = QF2_1
        else:
            SF1_2 = QF2_2
    print('______________________________')
    # Fim do jogo QF2

    # Jogo QF3
    print('______________________________')

    QF3 = resultado(int(QF3_1[1]), int(QF3_2[1]))

    print('\n{} {} x {} {}\n'.format(QF3_1[0],
                                     QF3[0], QF3[1], QF3_2[0]))

    # Estrutura de classificação:
    if QF3[0] > QF3[1]:
        SF2_1 = QF3_1
    elif QF3[0] < QF3[1]:
        SF2_1 = QF3_2
    else:
        print('\nNos penaltis:\n')
        QF3 = desempate()
        print('\n{} {} x {} {}\n'.format(QF3_1[0],
                                         QF3[0], QF3[1], QF3_2[0]))
        if QF3[0] > QF3[1]:
            SF2_1 = QF3_1
        else:
            SF2_1 = QF3_2
    print('______________________________')
    # Fim do jogo QF3

    # Jogo QF4
    print('______________________________')

    QF4 = resultado(int(QF4_1[1]), int(QF4_2[1]))

    print('\n{} {} x {} {}\n'.format(QF4_1[0],
                                     QF4[0], QF4[1], QF4_2[0]))

    # Estrutura de classificação:
    if QF4[0] > QF4[1]:
        SF2_2 = QF4_1
    elif QF4[0] < QF4[1]:
        SF2_2 = QF4_2
    else:
        print('\nNos penaltis:\n')
        QF4 = desempate()
        print('\n{} {} x {} {}\n'.format(QF4_1[0],
                                         QF4[0], QF4[1], QF4_2[0]))
        if QF4[0] > QF4[1]:
            SF2_2 = QF4_1
        else:
            SF2_2 = QF4_2
    print('______________________________')
    # Fim do jogo QF4

    # SEMI FINAL
    print('\n\n_____SEMI FINAL______\n\n')
    # Jogo SF1
    print('______________________________')

    SF1 = resultado(int(SF1_1[1]), int(SF1_2[1]))

    print('\n{} {} x {} {}\n'.format(SF1_1[0],
                                     SF1[0], SF1[1], SF1_2[0]))

    # Estrutura de classificação:
    if SF1[0] > SF1[1]:
        FINAL_1 = SF1_1
        TL1 = SF1_2
    elif SF1[0] < SF1[1]:
        FINAL_1 = SF1_2
        TL1 = SF1_1
    else:
        print('\nNos penaltis:\n')
        SF1 = desempate()
        print('\n{} {} x {} {}\n'.format(SF1_1[0],
                                         SF1[0], SF1[1], SF1_2[0]))
        if SF1[0] > SF1[1]:
            FINAL_1 = SF1_1
            TL1 = SF1_2
        else:
            FINAL_1 = SF1_2
            TL1 = SF1_1
    print('______________________________')
    # Fim do jogo SF1

    # Jogo SF2
    print('______________________________')

    SF2 = resultado(int(SF2_1[1]), int(SF2_2[1]))

    print('\n{} {} x {} {}\n'.format(SF2_1[0],
                                     SF2[0], SF2[1], SF2_2[0]))

    # Estrutura de classificação:
    if SF2[0] > SF2[1]:
        FINAL_2 = SF2_1
        TL2 = SF2_2
    elif SF2[0] < SF2[1]:
        FINAL_2 = SF2_2
        TL2 = SF2_1
    else:
        print('\nNos penaltis:\n')
        SF2 = desempate()
        print('\n{} {} x {} {}\n'.format(SF2_1[0],
                                         SF2[0], SF2[1], SF2_2[0]))
        if SF2[0] > SF2[1]:
            FINAL_2 = SF2_1
            TL2 = SF2_2
        else:
            FINAL_2 = SF2_2
            TL2 = SF2_1
    print('______________________________')
    # Fim do jogo SF2

    print('__DISPUTA DE TERCEIRO LUGAR__')
    # Jogo TL
    print('______________________________')

    TL = resultado(int(TL1[1]), int(TL2[1]))

    print('\n{} {} x {} {}\n'.format(TL1[0],
                                     TL[0], TL[1], TL2[0]))

    # Estrutura de classificação:
    if TL[0] > TL[1]:
        Terceiro = TL1
        Quarto = TL2

    elif TL[0] < TL[1]:
        Terceiro = TL2
        Quarto = TL1

    else:
        print('\nNos penaltis:\n')
        TL = desempate()
        print('\n{} {} x {} {}\n'.format(TL1[0],
                                         TL[0], TL[1], TL2[0]))
        if TL[0] > TL[1]:
            Terceiro = TL1
            Quarto = TL2

        else:
            Terceiro = TL2
            Quarto = TL1

    print('______________________________')
    # Fim do jogo TL

    print('__FINAL__')
    # Jogo final
    print('______________________________')

    final = resultado(int(FINAL_1[1]), int(FINAL_2[1]))

    print('\n{} {} x {} {}\n'.format(FINAL_1[0],
                                     final[0], final[1], FINAL_2[0]))

    # Estrutura de classificação:
    if final[0] > final[1]:
        Camp = FINAL_1
        Vice = FINAL_2
    elif final[0] < final[1]:
        Camp = FINAL_2
        Vice = FINAL_1
    else:
        print('\nNos penaltis:\n')
        final = desempate()
        print('\n{} {} x {} {}\n'.format(FINAL_1[0],
                                         final[0], final[1], FINAL_2[0]))
        if final[0] > final[1]:
            Camp = FINAL_1
            Vice = FINAL_2

        else:
            Camp = FINAL_2
            Vice = FINAL_1

    print('______________________________')
    # Fim do Mata Mata

    print('{} foi a seleção vencedora da Copa do Mundo!'.format(Camp))
    print('{} foi a seleção vice'.format(Vice))
    print('{} foi a seleção que ficou em terceiro'.format(Terceiro))
    print('{} foi a seleção que ficou em quarto'.format(Quarto))
