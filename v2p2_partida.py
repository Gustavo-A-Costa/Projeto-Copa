from random import randint, choice


def resultado(forcaA, forcaB, jogA, jogB, pro=False, dec=False):
    # zerando o relogio
    minutagem = 1

    # variaveis time A e B
    golsA, golsB = 0, 0
    coletivoA = (100*forcaA/(forcaA+forcaB))/3
    coletivoB = (100*forcaB/(forcaA+forcaB))/3
    ataqueA = randint(0, forcaA)
    ataqueB = randint(0, forcaB)
    defesaA = randint(0, forcaA + int(coletivoA))
    defesaB = randint(0, forcaB + int(coletivoB))
    meioA = randint(0, int((forcaA+ataqueA+defesaA)/3))
    meioB = randint(0, int((forcaB+ataqueB+defesaB)/3))
    # chance de cada jogador fazer gol - Goleiro = 1/343
    goljog = [10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8,
              10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8,
              10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8,
              10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8,
              10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8,
              10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8,
              10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8,
              10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8,
              10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8,
              10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8,
              10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8,
              10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8,
              7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4,
              7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4,
              7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4,
              7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4,
              7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4,
              7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4,
              7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4,
              7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4,
              7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4,
              3, 3, 3, 2, 2, 2, 1, 1, 1,
              3, 3, 3, 2, 2, 2, 1, 1, 1,
              3, 3, 3, 2, 2, 2, 1, 1, 1,
              3, 3, 3, 2, 2, 2, 1, 1, 1,
              3, 3, 3, 2, 2, 2, 1, 1, 1,
              3, 3, 3, 2, 2, 2, 1, 1, 1,
              0]
    # variaveis globais
    hora_do_golA = [1]
    hora_do_golB = [1]
    # len = 14 - 107 gols
    # len = 15 - 94 gols
    # len = 13 - 119 gols!!!! - 13 vai ser o nivel maximo
    # O hora do gol vai ser menor quanto mais alto o nivel (len = 1300/nivel)
    # ou seja, quanto maior o nivel, maior a chance de gol
    if dec is False:
        for k in range(0, int(1300/forcaA)):
            hora_do_golA.append(0)
            # print(hora_do_golA, k)
        for k in range(0, int(1300/forcaB)):
            hora_do_golB.append(0)
            # print(hora_do_golB, k)
    # print('Hora do Gol A e B finais acima!')

    if dec is True:
        for k in range(0, int(2200/forcaA)):
            hora_do_golA.append(0)
            # print(hora_do_golA, k)
        for k in range(0, int(2200/forcaB)):
            hora_do_golB.append(0)

    # p/ reduzir a chance de gol a cada chance, 1/len(hora)
    texto_GA = []
    texto_GB = []
    chanceA = choice(hora_do_golA)
    chanceB = choice(hora_do_golB)
    c_g_jog = choice(goljog)
    grp_acrescimos = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
                      2, 2, 2, 2, 2, 3, 3, 3, 3, 3,
                      4, 4, 4, 4, 4, 5, 5, 5, 5, 5,
                      6, 6, 7, 7, 8, 9, 10]
    acrescimos = choice(grp_acrescimos)

    tempo_jogo = 90 + acrescimos

# ____________________________ Jogo Normal __________________
    for minutagem in range(1, tempo_jogo):
        if meioA > (meioB - coletivoA/2) and meioB > (meioA - coletivoB/2):
            chanceA = 0
            chanceB = 0
        if (meioA > (meioB - coletivoA/2) and ataqueA > defesaB
                and chanceA == 1):
            golsA += 1
            texto_GA.append(f"{jogA[c_g_jog]}, {minutagem}'")
        if (meioB > (meioA - coletivoB/2) and ataqueB > defesaA
                and chanceB == 1):
            golsB += 1
            texto_GB.append(f"{jogB[c_g_jog]}, {minutagem}'")

        if golsA + golsB in range(2, 5) and minutagem % 5 == 0:
            hora_do_golA.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0])
            hora_do_golB.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0])
            # p/ diminuir qtd de goleadas bizarras

        if golsA + golsB > 6 and minutagem % 5 == 0:
            hora_do_golA.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0])
            hora_do_golB.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0])
            # p/ diminuir qtd de goleadas bizarras

        # resets:
        chanceA = choice(hora_do_golA)
        chanceB = choice(hora_do_golB)
        ataqueA = randint(0, forcaA)
        ataqueB = randint(0, forcaB)
        meioA = randint(0, forcaA)
        meioB = randint(0, forcaB)
        defesaA = randint(0, forcaA)
        defesaB = randint(0, forcaB)
        acrescimos = choice(grp_acrescimos)
        c_g_jog = choice(goljog)
        minutagem += 1

# ____________________________ Fim do Jogo Normal __________________
# ____________________________ Prorrogacao __________________
    if golsA == golsB and pro is True:
        for minutagem in range(tempo_jogo, tempo_jogo + 31):
            if meioA > (meioB - coletivoA) and meioB > (meioA - coletivoB):
                chanceA = 0
                chanceB = 0
            if (meioA > (meioB - coletivoA) and ataqueA > defesaB
                    and chanceA == 1):
                golsA += 1
                texto_GA.append(f"{jogA[c_g_jog]}, {minutagem}'(Pro)")
            if (meioB > (meioA - coletivoB) and ataqueB > defesaA
                    and chanceB == 1):
                golsB += 1
                texto_GB.append(f"{jogB[c_g_jog]}, {minutagem}'(Pro)")

            if golsA + golsB in range(2, 5) and minutagem % 5 == 0:
                hora_do_golA.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0, 0, 0])
                hora_do_golB.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0, 0, 0])
                # p/ diminuir qtd de goleadas bizarras

            if golsA + golsB > 6 and minutagem % 5 == 0:
                hora_do_golA.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0, 0, 0])
                hora_do_golB.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                     0, 0, 0])
                # p/ diminuir qtd de goleadas bizarras

            chanceA = choice(hora_do_golA)
            chanceB = choice(hora_do_golB)
            ataqueA = randint(0, forcaA)
            ataqueB = randint(0, forcaB)
            meioA = randint(0, forcaA)
            meioB = randint(0, forcaB)
            defesaA = randint(0, forcaA)
            defesaB = randint(0, forcaB)
            acrescimos = choice(grp_acrescimos)
            c_g_jog = choice(goljog)
            minutagem += 1
# ____________________________ Fim da Prorrogacao __________________

    if golsA == golsB:
        zz = randint(1, 2)
        # garante uma taxa de 0x0 em torno de 6 %
        if zz == 1:
            golsA, golsB = 0, 0
            texto_GA = []
            texto_GB = []

    minsA = ''
    minsB = ''

    for gol in texto_GA:
        minsA += f'| {gol} |'
    for gol in texto_GB:
        minsB += f'| {gol} |'

    if golsA == 0:
        minsA = 'Nenhum'

    if golsB == 0:
        minsB = 'Nenhum'

    return(golsA, golsB, minsA, minsB)


def vit_prob(val_jogo, iteracoes=100000):
    vit1 = 0
    vit2 = 0
    for joguitos in range(0, iteracoes):
        p = resultado(*val_jogo)
        if p[0] > p[1]:
            vit1 += 1
        elif p[1] > p[0]:
            vit2 += 1
    return [vit1, vit2]


if __name__ == '__main__':
    jogaA = ['Leo',
             'Brito', 'Eduardo', 'Bonini', 'Filipe',
             'Gustavo', 'Tamarindo', 'Carotta', 'P. Augusto',
             'Brayan', 'Carotta']
    jogaB = ['Buffon',
             'Marcelo', 'Sergio Ramos', 'Pique', 'Dani Alves',
             'Pelé', 'Iniesta', 'Messi', 'Cristiano',
             'Maradona', 'Garrincha']

    for teste1 in range(0, 10):
        for teste2 in range(0, 10):
            val_jogo = (teste1*10 + 9, teste2*10 + 9, jogaA, jogaB)
            final = vit_prob(val_jogo)
            print(f"""
            Nível {val_jogo[0]}: {final[0]} / Nível {val_jogo[1]}: {final[1]}'
            """)
