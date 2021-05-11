from random import randint, choice


def resultado(forcaA, forcaB):
    # zerando o relogio
    minutagem = 1

    # variaveis time A e B
    golsA, golsB = 0, 0
    ataqueA = randint(0, forcaA)
    ataqueB = randint(0, forcaB)
    meioA = randint(0, forcaA)
    meioB = randint(0, forcaB)
    defesaA = randint(0, forcaA)
    defesaB = randint(0, forcaB)

    # variaveis globais
    hora_do_gol = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    # p/ reduzir a chance de gol a cada chance, 1/len(hora)
    texto_GA = []
    texto_GB = []
    chance = choice(hora_do_gol)
    grp_acrescimos = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
                      2, 2, 2, 2, 2, 3, 3, 3, 3, 3,
                      4, 4, 4, 4, 4, 5, 5, 5, 5, 5,
                      6, 6, 7, 7, 8, 9, 10]
    acrescimos = choice(grp_acrescimos)

    for minutagem in range(1, 90 + acrescimos):
        if meioA > meioB and ataqueA > defesaB and chance == 1:
            golsA += 1
            texto_GA.append(f"{minutagem}'")
        if meioB > meioA and ataqueB > defesaA and chance == 1:
            golsB += 1
            texto_GB.append(f"{minutagem}'")

        if golsA + golsB in range(2, 5) and minutagem % 5 == 0:
            hora_do_gol.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0])
            # p/ diminuir qtd de goleadas bizarras

        if golsA + golsB > 6 and minutagem % 5 == 0:
            hora_do_gol.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0])
            # p/ diminuir qtd de goleadas bizarras

        # resets:
        chance = choice(hora_do_gol)
        ataqueA = randint(0, forcaA)
        ataqueB = randint(0, forcaB)
        meioA = randint(0, forcaA)
        meioB = randint(0, forcaB)
        defesaA = randint(0, forcaA)
        defesaB = randint(0, forcaB)
        acrescimos = choice(grp_acrescimos)
        minutagem += 1

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
        minsA += f'-{gol}'
    for gol in texto_GB:
        minsB += f'-{gol}'

    if golsA == 0 and golsB == 0:
        minsA = 'Nenhum'
        minsB = 'Nenhum'

    return(golsA, golsB, minsA, minsB)


if __name__ == '__main__':
    golsA = ''
    golsB = ''
    p = resultado(100, 40)
    print(f'França {p[0]} x {p[1]} Alemanha')
    print(f'Gols: {p[2]} / {p[3]}')
