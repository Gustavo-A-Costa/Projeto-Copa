# Código por Gustavo Albuquerque - 20/04/2021
from random import randint


def desempate():
    Prob_Pen = [0, 1, 1, 1]
    Pen_A = 0
    Pen_B = 0
    i = 0
    t = 0

    while i < 5:
        # aqui é para evitar diferenças grandes nos penaltis
        if (Pen_A + 5 - i) < Pen_B:
            break

        if (Pen_B + 5 - i) < Pen_A:
            break

        BatidaA = Prob_Pen[randint(0, 3)]
        if BatidaA == 1:
            Pen_A = Pen_A + 1

        BatidaB = Prob_Pen[randint(0, 3)]
        if BatidaB == 1:
            Pen_B = Pen_B + 1

        # print(Pen_A, Pen_B)

        i = i + 1

    # trecho das alternadas
    if Pen_A == Pen_B and i == 5:
        while t == 0:
            Pen_A = Pen_A + randint(0, 1)
            Pen_B = Pen_B + randint(0, 1)
            # print('Altern*', Pen_A, Pen_B)
            t = Pen_A - Pen_B

    return [Pen_A, Pen_B]
