# Código por Gustavo Albuquerque - 20/04/2021
from random import choice

# primeiro passo: marcar os potes para o sorteio
# seria legal colocar o país sede no topo!
# imprimir o resultado em um arquivo.txt seria muito bom também.


def sorteio_copa():
    print("Simulando...")
    lista10 = []
    erroc = 0
    errou = 0
    with open('copa.csv') as arquivo:
        dados = arquivo.read()
        # dados são linhas de string!
        #    for selecao in dados: aqui, como sel_dados são strings, um selecao
        #    in sel_dados é cada letra!

        #    for selecao in dados.split(','): Fazendo isso aqui, cada "Selecao"
        #    vira um item (str) depois da vírgula
        for selecao in dados.splitlines():  # as linhas são separadas aqui!
            dados_sel = list(selecao.split(','))
            # cada 'selecao é uma linha do arquivo. Para criar uma lista e
            # separar os conteúdos pelas virgulas, uso o split(',')
            dict_sel = {'País': dados_sel[0], 'Confederação': dados_sel[1],
                        'Nível': dados_sel[2], 'Sede?': dados_sel[3]}

            if 'sede' in dict_sel.get('Sede?'):
                pais_sede = dict_sel

            if 'sede' not in dict_sel.get('Sede?'):
                lista10.append(dict_sel)

    ordem = sorted(lista10, key=lambda k: k['Nível'])
    pote1 = [pais_sede, ordem[30], ordem[29], ordem[28],
             ordem[27], ordem[26], ordem[25], ordem[24]]
    pote2 = list(ordem[16:24])
    pote3 = list(ordem[8:16])
    pote4 = list(ordem[0:8])

    # print('O pote 1 consiste em:\n {} \n'.format(pote1))
    # print('O pote 2 consiste em:\n {} \n'.format(pote2))
    # print('O pote 3 consiste em:\n {} \n'.format(pote3))
    # print('O pote 4 consiste em:\n {} \n'.format(pote4))

    # agora vem a parte do sorteio
    # a ideia é pegar um time de cada pote. Pode haver, no maximo,
    # duas seleções da UEFA no mesmo grupo.

    # aqui eu defino numeros aleatórios que sejam diferentes, p/
    # sortear os grupos através dos indices dos potes

    # CICLO DE GERAÇÃO DE NUMÉROS ALEATÓRIOS
    pote1_sort = [1, 2, 3, 4, 5, 6, 7]
    alep1 = choice(pote1_sort)
    pote1_sort.remove(alep1)

    alep2 = choice(pote1_sort)
    pote1_sort.remove(alep2)

    alep3 = choice(pote1_sort)
    pote1_sort.remove(alep3)

    alep4 = choice(pote1_sort)
    pote1_sort.remove(alep4)

    alep5 = choice(pote1_sort)
    pote1_sort.remove(alep5)

    alep6 = choice(pote1_sort)
    pote1_sort.remove(alep6)

    alep7 = choice(pote1_sort)
    pote1_sort.remove(alep7)

    potes_sort = [0, 1, 2, 3, 4, 5, 6, 7]
    # posicoes do pote
    ale1 = choice(potes_sort)
    # print(ale1)
    potes_sort.remove(ale1)
    # print(potes_sort)
    # fim do primeiro ciclo
    ale2 = choice(potes_sort)
    # print(ale2)
    potes_sort.remove(ale2)
    # print(potes_sort)
    # fim do segundo ciclo
    ale3 = choice(potes_sort)
    # print(ale3)
    potes_sort.remove(ale3)
    # print(potes_sort)
    # fim do terceiro ciclo
    ale4 = choice(potes_sort)
    # print(ale4)
    potes_sort.remove(ale4)
    # print(potes_sort)
    # fim do quarto ciclo
    ale5 = choice(potes_sort)
    # print(ale5)
    potes_sort.remove(ale5)
    # print(potes_sort)
    # fim do quinto ciclo
    ale6 = choice(potes_sort)
    # print(ale6)
    potes_sort.remove(ale6)
    # print(potes_sort)
    # fim do sexto ciclo
    ale7 = choice(potes_sort)
    # print(ale7)
    potes_sort.remove(ale7)
    # print(potes_sort)
    # fim do sétimo ciclo
    ale8 = potes_sort[0]
    # print(ale8)
    potes_sort.remove(ale8)
    # print(potes_sort)
    # fim do oitavo ciclo

    grupoA = [pote1[0], pote2[ale8], pote3[ale7], pote4[ale6]]
    grupoB = [pote1[alep1], pote2[ale7], pote3[ale5], pote4[ale4]]
    grupoC = [pote1[alep2], pote2[ale6], pote3[ale3], pote4[ale2]]
    grupoD = [pote1[alep3], pote2[ale5], pote3[ale1], pote4[ale8]]
    grupoE = [pote1[alep4], pote2[ale4], pote3[ale8], pote4[ale1]]
    grupoF = [pote1[alep5], pote2[ale3], pote3[ale4], pote4[ale3]]
    grupoG = [pote1[alep6], pote2[ale2], pote3[ale6], pote4[ale5]]
    grupoH = [pote1[alep7], pote2[ale1], pote3[ale2], pote4[ale7]]

    # Grupos contendo apenas as confederações dos países escolhidos
    confgrupoA = [pote1[0]['Confederação'], pote2[ale8]['Confederação'],
                  pote3[ale7]['Confederação'], pote4[ale6]['Confederação']]
    confgrupoB = [pote1[alep1]['Confederação'], pote2[ale7]['Confederação'],
                  pote3[ale5]['Confederação'], pote4[ale4]['Confederação']]
    confgrupoC = [pote1[alep2]['Confederação'], pote2[ale6]['Confederação'],
                  pote3[ale3]['Confederação'], pote4[ale2]['Confederação']]
    confgrupoD = [pote1[alep3]['Confederação'], pote2[ale5]['Confederação'],
                  pote3[ale1]['Confederação'], pote4[ale8]['Confederação']]
    confgrupoE = [pote1[alep4]['Confederação'], pote2[ale4]['Confederação'],
                  pote3[ale8]['Confederação'], pote4[ale1]['Confederação']]
    confgrupoF = [pote1[alep5]['Confederação'], pote2[ale3]['Confederação'],
                  pote3[ale4]['Confederação'], pote4[ale3]['Confederação']]
    confgrupoG = [pote1[alep6]['Confederação'], pote2[ale2]['Confederação'],
                  pote3[ale6]['Confederação'], pote4[ale5]['Confederação']]
    confgrupoH = [pote1[alep7]['Confederação'], pote2[ale1]['Confederação'],
                  pote3[ale2]['Confederação'], pote4[ale7]['Confederação']]
    # print('O Grupo A é: \n {}'.format(grupoA))
    # print('O Grupo B é: \n {}'.format(grupoB))
    # print('O Grupo C é: \n {}'.format(grupoC))
    # print('O Grupo D é: \n {}'.format(grupoD))
    # print('O Grupo E é: \n {}'.format(grupoE))
    # print('O Grupo F é: \n {}'.format(grupoF))
    # print('O Grupo G é: \n {}'.format(grupoG))
    # print('O Grupo H é: \n {}'.format(grupoH))

    # VERIFICANDO SE HÁ NO MÁXIMO DOIS TIMES UEFA NO MESMO GRUPO
    # GRUPO A
    SA_UEFA = confgrupoA.count(' UEFA')
    SA_CAF = confgrupoA.count(' CAF')
    SA_CONMEBOL = confgrupoA.count(' CONMEBOL')
    SA_AFC = confgrupoA.count(' AFC')
    SA_CONCACAF = confgrupoA.count(' CONCACAF')
    SA_OFC = confgrupoA.count(' OFC')

    # GRUPO B
    SB_UEFA = confgrupoB.count(' UEFA')
    SB_CAF = confgrupoB.count(' CAF')
    SB_CONMEBOL = confgrupoB.count(' CONMEBOL')
    SB_AFC = confgrupoB.count(' AFC')
    SB_CONCACAF = confgrupoB.count(' CONCACAF')
    SB_OFC = confgrupoB.count(' OFC')

    # GRUPO C
    SC_UEFA = confgrupoC.count(' UEFA')
    SC_CAF = confgrupoC.count(' CAF')
    SC_CONMEBOL = confgrupoC.count(' CONMEBOL')
    SC_AFC = confgrupoC.count(' AFC')
    SC_CONCACAF = confgrupoC.count(' CONCACAF')
    SC_OFC = confgrupoC.count(' OFC')

    # GRUPO D
    SD_UEFA = confgrupoD.count(' UEFA')
    SD_CAF = confgrupoD.count(' CAF')
    SD_CONMEBOL = confgrupoD.count(' CONMEBOL')
    SD_AFC = confgrupoD.count(' AFC')
    SD_CONCACAF = confgrupoD.count(' CONCACAF')
    SD_OFC = confgrupoD.count(' OFC')

    # GRUPO E
    SE_UEFA = confgrupoE.count(' UEFA')
    SE_CAF = confgrupoE.count(' CAF')
    SE_CONMEBOL = confgrupoE.count(' CONMEBOL')
    SE_AFC = confgrupoE.count(' AFC')
    SE_CONCACAF = confgrupoE.count(' CONCACAF')
    SE_OFC = confgrupoE.count(' OFC')

    # GRUPO F
    SF_UEFA = confgrupoF.count(' UEFA')
    SF_CAF = confgrupoF.count(' CAF')
    SF_CONMEBOL = confgrupoF.count(' CONMEBOL')
    SF_AFC = confgrupoF.count(' AFC')
    SF_CONCACAF = confgrupoF.count(' CONCACAF')
    SF_OFC = confgrupoF.count(' OFC')

    # GRUPO G
    SG_UEFA = confgrupoG.count(' UEFA')
    SG_CAF = confgrupoG.count(' CAF')
    SG_CONMEBOL = confgrupoG.count(' CONMEBOL')
    SG_AFC = confgrupoG.count(' AFC')
    SG_CONCACAF = confgrupoG.count(' CONCACAF')
    SG_OFC = confgrupoG.count(' OFC')

    # GRUPO H
    SH_UEFA = confgrupoH.count(' UEFA')
    SH_CAF = confgrupoH.count(' CAF')
    SH_CONMEBOL = confgrupoH.count(' CONMEBOL')
    SH_AFC = confgrupoH.count(' AFC')
    SH_CONCACAF = confgrupoH.count(' CONCACAF')
    SH_OFC = confgrupoH.count(' OFC')

    if (SA_UEFA > 2 or SB_UEFA > 2 or SC_UEFA > 2 or SD_UEFA > 2 or
            SE_UEFA > 2 or SF_UEFA > 2 or SG_UEFA > 2 or SH_UEFA > 2):
        # print('\nEXCESSO DE UEFA EM GRUPO / Sorteio em repetição\n')
        errou = 1

    elif (SA_CAF > 1 or SB_CAF > 1 or SC_CAF > 1 or SD_CAF > 1 or
          SE_CAF > 1 or SF_CAF > 1 or SG_CAF > 1 or SH_CAF > 1 or
          SA_CONMEBOL > 1 or SB_CONMEBOL > 1 or SC_CONMEBOL > 1 or
          SD_CONMEBOL > 1 or SE_CONMEBOL > 1 or SF_CONMEBOL > 1 or
          SG_CONMEBOL > 1 or SH_CONMEBOL > 1 or SA_AFC > 1 or
          SB_AFC > 1 or SC_AFC > 1 or SD_AFC > 1 or SE_AFC > 1 or
          SF_AFC > 1 or SG_AFC > 1 or SH_AFC > 1 or
          SA_CONCACAF > 1 or SB_CONCACAF > 1 or SC_CONCACAF > 1 or
          SD_CONCACAF > 1 or SE_CONCACAF > 1 or SF_CONCACAF > 1 or
          SG_CONCACAF > 1 or SH_CONCACAF > 1 or SA_OFC > 1 or SB_OFC > 1 or
          SC_OFC > 1 or SD_OFC > 1 or SE_OFC > 1 or SF_OFC > 1 or
            SG_OFC > 1 or SH_OFC > 1):
        # print('\nEXCESSO DE CONFEDERAÇÃO EM GRUPO / Sorteio em repetição\n')
        erroc = 1

    if (erroc == 1 or errou == 1):
        # print('Repetindo...\n')
        return sorteio_copa()

    else:
        print('Copa organizada e simulada com sucesso!')
        print('Abrindo janela...')
        return [grupoA, grupoB, grupoC, grupoD, grupoE, grupoF, grupoG, grupoH]


def texto_sorteio(dados):
    textoA = f"""
    Grupo A:
    {dados[0][0]['País']}
    {dados[0][1]['País']}
    {dados[0][2]['País']}
    {dados[0][3]['País']}\n
    """
    textoB = f"""
    Grupo B:
    {dados[1][0]['País']}
    {dados[1][1]['País']}
    {dados[1][2]['País']}
    {dados[1][3]['País']}\n
    """
    textoC = f"""
    Grupo C:
    {dados[2][0]['País']}
    {dados[2][1]['País']}
    {dados[2][2]['País']}
    {dados[2][3]['País']}\n
    """
    textoD = f"""
    Grupo D:
    {dados[3][0]['País']}
    {dados[3][1]['País']}
    {dados[3][2]['País']}
    {dados[3][3]['País']}\n
    """
    textoE = f"""
    Grupo E:
    {dados[4][0]['País']}
    {dados[4][1]['País']}
    {dados[4][2]['País']}
    {dados[4][3]['País']}\n
    """
    textoF = f"""
    Grupo F:
    {dados[5][0]['País']}
    {dados[5][1]['País']}
    {dados[5][2]['País']}
    {dados[5][3]['País']}\n
    """
    textoG = f"""
    Grupo G:
    {dados[6][0]['País']}
    {dados[6][1]['País']}
    {dados[6][2]['País']}
    {dados[6][3]['País']}\n
    """
    textoH = f"""
    Grupo H:
    {dados[7][0]['País']}
    {dados[7][1]['País']}
    {dados[7][2]['País']}
    {dados[7][3]['País']}\n
    """
    return [textoA, textoB, textoC, textoD,
            textoE, textoF, textoG, textoH]


# FIM DA FUNÇÃO SORTEIO
if __name__ == '__main__':

    grupos = sorteio_copa()
    GA = grupos[0]
    GB = grupos[1]
    GC = grupos[2]
    GD = grupos[3]
    GE = grupos[4]
    GF = grupos[5]
    GG = grupos[6]
    GH = grupos[7]

    print('Grupo A:\n{}\n'.format(GA))
    print('Grupo B:\n{}\n'.format(GB))
    print('Grupo C:\n{}\n'.format(GC))
    print('Grupo D:\n{}\n'.format(GD))
    print('Grupo E:\n{}\n'.format(GE))
    print('Grupo F:\n{}\n'.format(GF))
    print('Grupo G:\n{}\n'.format(GG))
    print('Grupo H:\n{}\n'.format(GH))
