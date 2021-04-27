# Código por Gustavo Albuquerque - 20/04/2021
from random import randint

# i = 0
# VITA = 0
# VITB = 0
# EMP = 0


def resultado(ForcaA, ForcaB):

    # difAB = ForcaA - ForcaB
    # difBA = ForcaB - ForcaA

    # if difAB < 0:
    #     difAB = 0

    # if difBA < 0:
    #     difBA = 0

    # Modo 2:
    espaco = ForcaA + ForcaB

    sorteA = randint(0, ForcaA)
    golA = int(sorteA * ((ForcaA + randint(0, 10 - ForcaB))/espaco))

    sorteB = randint(0, ForcaB)
    golB = int(sorteB * ((ForcaB + randint(0, 10 - ForcaA))/espaco))

    if golA < 0:
        golA = 0

    if golB < 0:
        golB = 0

    return [golA, golB]


"""
while i < 10:
    score = placar(10, 7)
    golFA = score[0]
    golBA = score[1]
    print('{} {} x {} {}'.format('Portugal', golFA, golBA, 'Japão'))
    i = i + 1

    if golFA > golBA:
        VITA = VITA + 1
    if golBA > golFA:
        VITB = VITB + 1
    if golBA == golFA:
        EMP = EMP + 1

    print('\nVitórias Portugal: {}\n'.format(VITA))
    print('\nVitórias Japão: {}\n'.format(VITB))
    print('\nEmpates: {}\n'.format(EMP))
"""
