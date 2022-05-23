# Código por Gustavo Albuquerque - 10/2021
from sys import getfilesystemencoding
from PySimpleGUI import PySimpleGUI as sg
from sorteio import sorteio_copa, texto_sorteio
from v2_simulador_grupos import tabela_grupos, textos_grupo
from v2_matamata import copa_mundo, textos_matamata
from collections import Counter
import re
import operator

# fonte
ft = 'Bahnschrift'

# tamanho da janela
tam = (1000, 1000)

# artilharia
autores_gols = []
paises_GA = []
paises_GB = []
paises_GC = []
paises_GD = []
paises_GE = []
paises_GF = []
paises_GG = []
paises_GH = []
paises_oitavas = []
paises_quartas = []
paises_semi = []
paises_terceiro = []
paises_final = []

grupos = sorteio_copa()
GA = tabela_grupos(grupos[0])
GB = tabela_grupos(grupos[1])
GC = tabela_grupos(grupos[2])
GD = tabela_grupos(grupos[3])
GE = tabela_grupos(grupos[4])
GF = tabela_grupos(grupos[5])
GG = tabela_grupos(grupos[6])
GH = tabela_grupos(grupos[7])
sor_txt = texto_sorteio(grupos)
copa = copa_mundo(grupos, GA, GB, GC, GD, GE, GF, GG, GH)
oit1, oit2, oit3, oit4, qua1, qua2, sem, ter, fin = textos_matamata(*copa)

lg = [GA, GB, GC, GD, GE, GF, GG, GH]
lf = [oit1, oit2, oit3, oit4, qua1, qua2, sem, ter, fin]
lgru = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
lfas = ['Oitavas de Final 1/4', 'Oitavas de Final 2/4', 'Oitavas de Final 3/4',
        'Oitavas de Final 4/4', 'Quartas de Final 1/2', 'Quartas de Final 2/2',
        'Semi-Final', 'Decisão de 3º Lugar', 'Final']
i = 0
j = 0

topo = f'Grupo {lgru[i]}'
topo2 = f'{lfas[j]}'

# __________________modulo artilharia1 grupo a

for selecoes in grupos[0]:
        paises_GA.append(selecoes['País'])

# time 1 jogo 1
for jog in GA[2][0].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GA[0][0:3].upper()
                )

# time 2 jogo 1
for jog in GA[2][1].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GA[1][0:3].upper()
                )

# time 1 jogo 2
for jog in GA[2][2].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GA[2][0:3].upper()
                )

# time 2 jogo 2
for jog in GA[2][3].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GA[3][0:3].upper()
                )

# time 1 jogo 3
for jog in GA[2][4].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GA[0][0:3].upper()
                )

# time 2 jogo 3
for jog in GA[2][5].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GA[2][0:3].upper()
                )

# time 1 jogo 4
for jog in GA[2][6].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GA[1][0:3].upper()
                )

# time 2 jogo 4
for jog in GA[2][7].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GA[3][0:3].upper()
                )

# time 1 jogo 5
for jog in GA[2][8].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GA[0][0:3].upper()
                )

# time 2 jogo 5
for jog in GA[2][9].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GA[3][0:3].upper()
                )

# time 1 jogo 6
for jog in GA[2][10].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GA[1][0:3].upper()
                )

# time 2 jogo 6
for jog in GA[2][11].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GA[2][0:3].upper()
                )

# _________________-fim do modulo a

# __________________modulo artilharia1 grupo B

for selecoes in grupos[1]:
        paises_GB.append(selecoes['País'])

# time 1 jogo 1
for jog in GB[2][0].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GB[0][0:3].upper()
                )

# time 2 jogo 1
for jog in GB[2][1].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GB[1][0:3].upper()
                )

# time 1 jogo 2
for jog in GB[2][2].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GB[2][0:3].upper()
                )

# time 2 jogo 2
for jog in GB[2][3].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GB[3][0:3].upper()
                )

# time 1 jogo 3
for jog in GB[2][4].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GB[0][0:3].upper()
                )

# time 2 jogo 3
for jog in GB[2][5].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GB[2][0:3].upper()
                )

# time 1 jogo 4
for jog in GB[2][6].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GB[1][0:3].upper()
                )

# time 2 jogo 4
for jog in GB[2][7].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GB[3][0:3].upper()
                )

# time 1 jogo 5
for jog in GB[2][8].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GB[0][0:3].upper()
                )

# time 2 jogo 5
for jog in GB[2][9].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GB[3][0:3].upper()
                )

# time 1 jogo 6
for jog in GB[2][10].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GB[1][0:3].upper()
                )

# time 2 jogo 6
for jog in GB[2][11].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GB[2][0:3].upper()
                )

# _________________-fim do modulo B

# __________________modulo artilharia1 grupo C

for selecoes in grupos[2]:
        paises_GC.append(selecoes['País'])

# time 1 jogo 1
for jog in GC[2][0].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GC[0][0:3].upper()
                )

# time 2 jogo 1
for jog in GC[2][1].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GC[1][0:3].upper()
                )

# time 1 jogo 2
for jog in GC[2][2].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GC[2][0:3].upper()
                )

# time 2 jogo 2
for jog in GC[2][3].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GC[3][0:3].upper()
                )

# time 1 jogo 3
for jog in GC[2][4].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GC[0][0:3].upper()
                )

# time 2 jogo 3
for jog in GC[2][5].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GC[2][0:3].upper()
                )

# time 1 jogo 4
for jog in GC[2][6].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GC[1][0:3].upper()
                )

# time 2 jogo 4
for jog in GC[2][7].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GC[3][0:3].upper()
                )

# time 1 jogo 5
for jog in GC[2][8].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GC[0][0:3].upper()
                )

# time 2 jogo 5
for jog in GC[2][9].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GC[3][0:3].upper()
                )

# time 1 jogo 6
for jog in GC[2][10].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GC[1][0:3].upper()
                )

# time 2 jogo 6
for jog in GC[2][11].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GC[2][0:3].upper()
                )

# _________________-fim do modulo C
# __________________modulo artilharia1 grupo D

for selecoes in grupos[3]:
        paises_GD.append(selecoes['País'])

# time 1 jogo 1
for jog in GD[2][0].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GD[0][0:3].upper()
                )

# time 2 jogo 1
for jog in GD[2][1].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GD[1][0:3].upper()
                )

# time 1 jogo 2
for jog in GD[2][2].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GD[2][0:3].upper()
                )

# time 2 jogo 2
for jog in GD[2][3].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GD[3][0:3].upper()
                )

# time 1 jogo 3
for jog in GD[2][4].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GD[0][0:3].upper()
                )

# time 2 jogo 3
for jog in GD[2][5].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GD[2][0:3].upper()
                )

# time 1 jogo 4
for jog in GD[2][6].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GD[1][0:3].upper()
                )

# time 2 jogo 4
for jog in GD[2][7].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GD[3][0:3].upper()
                )

# time 1 jogo 5
for jog in GD[2][8].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GD[0][0:3].upper()
                )

# time 2 jogo 5
for jog in GD[2][9].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GD[3][0:3].upper()
                )

# time 1 jogo 6
for jog in GD[2][10].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GD[1][0:3].upper()
                )

# time 2 jogo 6
for jog in GD[2][11].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GD[2][0:3].upper()
                )

# _________________-fim do modulo D

# __________________modulo artilharia1 grupo E

for selecoes in grupos[4]:
        paises_GE.append(selecoes['País'])

# time 1 jogo 1
for jog in GE[2][0].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GE[0][0:3].upper()
                )

# time 2 jogo 1
for jog in GE[2][1].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GE[1][0:3].upper()
                )

# time 1 jogo 2
for jog in GE[2][2].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GE[2][0:3].upper()
                )

# time 2 jogo 2
for jog in GE[2][3].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GE[3][0:3].upper()
                )

# time 1 jogo 3
for jog in GE[2][4].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GE[0][0:3].upper()
                )

# time 2 jogo 3
for jog in GE[2][5].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GE[2][0:3].upper()
                )

# time 1 jogo 4
for jog in GE[2][6].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GE[1][0:3].upper()
                )

# time 2 jogo 4
for jog in GE[2][7].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GE[3][0:3].upper()
                )

# time 1 jogo 5
for jog in GE[2][8].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GE[0][0:3].upper()
                )

# time 2 jogo 5
for jog in GE[2][9].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GE[3][0:3].upper()
                )

# time 1 jogo 6
for jog in GE[2][10].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GE[1][0:3].upper()
                )

# time 2 jogo 6
for jog in GE[2][11].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GE[2][0:3].upper()
                )

# _________________-fim do modulo E
# __________________modulo artilharia1 grupo F

for selecoes in grupos[5]:
        paises_GF.append(selecoes['País'])

# time 1 jogo 1
for jog in GF[2][0].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GF[0][0:3].upper()
                )

# time 2 jogo 1
for jog in GF[2][1].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GF[1][0:3].upper()
                )

# time 1 jogo 2
for jog in GF[2][2].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GF[2][0:3].upper()
                )

# time 2 jogo 2
for jog in GF[2][3].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GF[3][0:3].upper()
                )

# time 1 jogo 3
for jog in GF[2][4].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GF[0][0:3].upper()
                )

# time 2 jogo 3
for jog in GF[2][5].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GF[2][0:3].upper()
                )

# time 1 jogo 4
for jog in GF[2][6].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GF[1][0:3].upper()
                )

# time 2 jogo 4
for jog in GF[2][7].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GF[3][0:3].upper()
                )

# time 1 jogo 5
for jog in GF[2][8].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GF[0][0:3].upper()
                )

# time 2 jogo 5
for jog in GF[2][9].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GF[3][0:3].upper()
                )

# time 1 jogo 6
for jog in GF[2][10].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GF[1][0:3].upper()
                )

# time 2 jogo 6
for jog in GF[2][11].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GF[2][0:3].upper()
                )

# _________________-fim do modulo F

# __________________modulo artilharia1 grupo G

for selecoes in grupos[6]:
        paises_GG.append(selecoes['País'])

# time 1 jogo 1
for jog in GG[2][0].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GG[0][0:3].upper()
                )

# time 2 jogo 1
for jog in GG[2][1].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GG[1][0:3].upper()
                )

# time 1 jogo 2
for jog in GG[2][2].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GG[2][0:3].upper()
                )

# time 2 jogo 2
for jog in GG[2][3].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GG[3][0:3].upper()
                )

# time 1 jogo 3
for jog in GG[2][4].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GG[0][0:3].upper()
                )

# time 2 jogo 3
for jog in GG[2][5].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GG[2][0:3].upper()
                )

# time 1 jogo 4
for jog in GG[2][6].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GG[1][0:3].upper()
                )

# time 2 jogo 4
for jog in GG[2][7].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GG[3][0:3].upper()
                )

# time 1 jogo 5
for jog in GG[2][8].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GG[0][0:3].upper()
                )

# time 2 jogo 5
for jog in GG[2][9].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GG[3][0:3].upper()
                )

# time 1 jogo 6
for jog in GG[2][10].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GG[1][0:3].upper()
                )

# time 2 jogo 6
for jog in GG[2][11].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GG[2][0:3].upper()
                )

# _________________-fim do modulo G

# __________________modulo artilharia1 grupo H

for selecoes in grupos[7]:
        paises_GH.append(selecoes['País'])

# time 1 jogo 1
for jog in GH[2][0].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GH[0][0:3].upper()
                )

# time 2 jogo 1
for jog in GH[2][1].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GH[1][0:3].upper()
                )

# time 1 jogo 2
for jog in GH[2][2].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GH[2][0:3].upper()
                )

# time 2 jogo 2
for jog in GH[2][3].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GH[3][0:3].upper()
                )

# time 1 jogo 3
for jog in GH[2][4].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GH[0][0:3].upper()
                )

# time 2 jogo 3
for jog in GH[2][5].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GH[2][0:3].upper()
                )

# time 1 jogo 4
for jog in GH[2][6].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GH[1][0:3].upper()
                )

# time 2 jogo 4
for jog in GH[2][7].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GH[3][0:3].upper()
                )

# time 1 jogo 5
for jog in GH[2][8].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GH[0][0:3].upper()
                )

# time 2 jogo 5
for jog in GH[2][9].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GH[3][0:3].upper()
                )

# time 1 jogo 6
for jog in GH[2][10].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GH[1][0:3].upper()
                )

# time 2 jogo 6
for jog in GH[2][11].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_GH[2][0:3].upper()
                )

# _________________-fim do modulo H

# print(Counter(autores_gols))

# print(copa[36]) -> Contém os autores dos gols do mata mata

# __________ Modulo Mata Mata _______
# OITAVAS Jogo 1
for sel2 in copa[0].split(" x "):
        paises_oitavas.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][0].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[0][0:3].upper()
                )

# time 2
for jog in copa[36][1].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[1][0:3].upper()
                )

# OITAVAS Jogo 2
for sel2 in copa[1].split(" x "):
        paises_oitavas.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][2].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[2][0:3].upper()
                )

# time 2
for jog in copa[36][3].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[3][0:3].upper()
                )

# OITAVAS Jogo 3
for sel2 in copa[2].split(" x "):
        paises_oitavas.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][4].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[4][0:3].upper()
                )

# time 2
for jog in copa[36][5].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[5][0:3].upper()
                )

# OITAVAS Jogo 4
for sel2 in copa[3].split(" x "):
        paises_oitavas.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][6].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[6][0:3].upper()
                )

# time 2
for jog in copa[36][7].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[7][0:3].upper()
                )

# OITAVAS Jogo 5
for sel2 in copa[4].split(" x "):
        paises_oitavas.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][8].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[8][0:3].upper()
                )

# time 2
for jog in copa[36][9].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[9][0:3].upper()
                )

# OITAVAS Jogo 6
for sel2 in copa[5].split(" x "):
        paises_oitavas.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][10].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[10][0:3].upper()
                )

# time 2
for jog in copa[36][11].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[11][0:3].upper()
                )

# OITAVAS Jogo 7
for sel2 in copa[6].split(" x "):
        paises_oitavas.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][12].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[12][0:3].upper()
                )

# time 2
for jog in copa[36][13].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[13][0:3].upper()
                )

# OITAVAS Jogo 8
for sel2 in copa[7].split(" x "):
        paises_oitavas.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][14].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[14][0:3].upper()
                )

# time 2
for jog in copa[36][15].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_oitavas[15][0:3].upper()
                )

# QUARTAS Jogo 1
for sel2 in copa[16].split(" x "):
        paises_quartas.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][16].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_quartas[0][0:3].upper()
                )

# time 2
for jog in copa[36][17].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_quartas[1][0:3].upper()
                )

# QUARTAS Jogo 2
for sel2 in copa[17].split(" x "):
        paises_quartas.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][18].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_quartas[2][0:3].upper()
                )

# time 2
for jog in copa[36][19].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_quartas[3][0:3].upper()
                )

# QUARTAS Jogo 3
for sel2 in copa[18].split(" x "):
        paises_quartas.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][20].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_quartas[4][0:3].upper()
                )

# time 2
for jog in copa[36][21].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_quartas[5][0:3].upper()
                )

# QUARTAS Jogo 4
for sel2 in copa[19].split(" x "):
        paises_quartas.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][22].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_quartas[6][0:3].upper()
                )

# time 2
for jog in copa[36][23].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_quartas[7][0:3].upper()
                )

# SEMI FINAL 1
for sel2 in copa[20].split(" x "):
        paises_semi.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][24].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_semi[0][0:3].upper()
                )

# time 2
for jog in copa[36][25].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_semi[1][0:3].upper()
                )

# SEMI FINAL 2
for sel2 in copa[21].split(" x "):
        paises_semi.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][26].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_semi[2][0:3].upper()
                )

# time 2
for jog in copa[36][27].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_semi[3][0:3].upper()
                )

# TERCEIRO LUGAR
for sel2 in copa[22].split(" x "):
        paises_terceiro.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][28].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_terceiro[0][0:3].upper()
                )

# time 2
for jog in copa[36][29].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_terceiro[1][0:3].upper()
                )

# FINAL
for sel2 in copa[23].split(" x "):
        paises_final.append(
                re.sub('[^a-zA-Z]+', '', sel2))
# time 1
for jog in copa[36][30].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_final[0][0:3].upper()
                )

# time 2
for jog in copa[36][31].split("||"):
        autores_gols.append(
                re.sub('[^a-zA-Z]+', '', jog) +
                " - " +
                paises_final[1][0:3].upper()
                )

# remove os nenhuns
autores_gols[:] = [x for x in autores_gols if "Nenhum" not in x]

tira_prorrog = []

tira_prorrog[:] = [x for x in autores_gols if "Prorrogacao" in x]

tira_prorrog2 = []


for sel3 in tira_prorrog:
        sel3 = re.sub('Prorrogacao', '', sel3)
        tira_prorrog2.append(sel3)

autores_gols += tira_prorrog2

autores_gols[:] = [x for x in autores_gols if "Prorrogacao" not in x]

# layout
sg.theme('Dark Brown 1')
menu_principal = [
                 [sg.Text('\n\n\n',
                          size=(10000, 1),
                          justification='center', font=ft)],
                 [sg.Text('SIMULADOR DE COPA DO MUNDO',
                          size=(10000, 1),
                          justification='center', font=(ft, 25))],
                 [sg.Text('v2.5',
                          size=(5, 2),
                          justification='center', font=(ft, 40))],
                 [sg.Radio('Resolução 1: 600x700', "RADIO1", default=False,
                           size=(22, 4), font=ft, key="RES1")],
                 [sg.Radio('Resolução 2: 1200x700', "RADIO1", default=True,
                           size=(22, 4), font=ft, key="RES2")],
                 [sg.Radio('Resolução 3: 1600x900', "RADIO1", default=False,
                           size=(22, 4), font=ft, key="RES3")],
                 [sg.Text('\n\n\n',
                          size=(10000, 1),
                          justification='center', font=ft)],               
                 [sg.Button('Começar!', font=(ft, 25), size=(10, 2))],
                 [sg.Text('\n\n\n',
                          size=(10000, 1),
                          justification='center', font=ft)],
                 [sg.Text('Gustavo Albuquerque - V2.40: 05/2021 / 2.5: 10/2021',
                          size=(1000, 1),
                          justification='center', font=ft)],
]

layout = menu_principal
# janela
janela = sg.Window('Simulador de Copa do Mundo V2.5', layout,
                   element_justification='c', size=(600,600))

cabecalho = ['País', 'Pontos', 'G. F.', 'G. S.', 'S. G.']
# eventos
while True:
    eventos, valores = janela.read()
    if eventos == 'Começar!':
        layout = [
            [sg.Text('Grupos Sorteados:',
                     font=ft)],
            [sg.Text(sor_txt[0],
                     justification='center', font=ft),
             sg.Text(sor_txt[1],
                     justification='center', font=ft),
             sg.Text(sor_txt[2],
                     justification='center', font=ft),
             sg.Text(sor_txt[3],
                     justification='center', font=ft)],
            [sg.Text(sor_txt[4],
                     justification='center', font=ft),
             sg.Text(sor_txt[5],
                     justification='center', font=ft),
             sg.Text(sor_txt[6],
                     justification='center', font=ft),
             sg.Text(sor_txt[7],
                     justification='center', font=ft)],
            [sg.Button('Continuar!')]
        ]
        if valores["RES1"] is True:
                tam = (600, 700)
        elif valores["RES2"] is True:
                tam = (1200, 700)
        elif valores["RES3"] is True:
                tam = (1600, 900)
        elif valores["TELA"] is True:
                tam = "tela cheia"
                
        janela.close()
        janela = sg.Window('Simulador de Copa do Mundo Beta V2.5',
                           layout, element_justification='c', size=tam)
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Continuar!':
        layout = [
            [sg.Text(topo,
                     font=ft)],
            [sg.Table(textos_grupo(*(lg[i]))[0],
                      headings=cabecalho,
                      auto_size_columns=True, hide_vertical_scroll=True,
                      font=ft, num_rows=4,
                      justification='left')],
            [sg.Text(textos_grupo(*(lg[i]))[1], size=(30, 18),
                     justification='center', font=ft),
             sg.Text(textos_grupo(*(lg[i]))[2], size=(30, 18),
                     justification='center', font=ft),
             sg.Text(textos_grupo(*(lg[i]))[3], size=(30, 18),
                     justification='center', font=ft)],
            [sg.Button('Próximo')]
        ]
        janela.close()
        janela = sg.Window('Simulador de Copa do Mundo Beta V2.5',
                           layout, element_justification='c', size=tam)

    if eventos == 'Próximo':
        i = i + 1
        topo = f'Grupo {lgru[i]}'
        layout = [
            [sg.Text(topo,
                     font=ft)],
            [sg.Table(textos_grupo(*(lg[i]))[0],
                      headings=cabecalho,
                      auto_size_columns=True, hide_vertical_scroll=True,
                      font=ft, num_rows=4,
                      justification='left')],
            [sg.Text(textos_grupo(*(lg[i]))[1], size=(30, 18),
                     justification='center', font=ft),
             sg.Text(textos_grupo(*(lg[i]))[2], size=(30, 18),
                     justification='center', font=ft),
             sg.Text(textos_grupo(*(lg[i]))[3], size=(30, 18),
                     justification='center', font=ft)],
            [sg.Button('Voltar'), sg.Text('      '), sg.Button('Próximo')]
        ]
        janela.close()
        janela = sg.Window('Simulador de Copa do Mundo Beta V2.5',
                           layout, element_justification='c', size=tam)

    if eventos == 'Voltar':
        if i != 0:
            j = 0
            i = i - 1
            topo = f'Grupo {lgru[i]}'
            layout = [
                [sg.Text(topo,
                         font=ft)],
                [sg.Table(textos_grupo(*(lg[i]))[0],
                          headings=cabecalho,
                          auto_size_columns=True, hide_vertical_scroll=True,
                          font=ft, num_rows=4,
                          justification='left')],
                [sg.Text(textos_grupo(*(lg[i]))[1], size=(30, 18),
                         justification='center', font=ft),
                 sg.Text(textos_grupo(*(lg[i]))[2], size=(30, 18),
                         justification='center', font=ft),
                 sg.Text(textos_grupo(*(lg[i]))[3], size=(30, 18),
                         justification='center', font=ft)],
                [sg.Button('Voltar'), sg.Text('      '), sg.Button('Próximo')]
            ]
            janela.close()
            janela = sg.Window('Simulador de Copa do Mundo Beta V2.5',
                               layout, element_justification='c', size=tam)

    if i == 7:
        layout = [
            [sg.Text(topo,
                     font=ft)],
            [sg.Table(textos_grupo(*(lg[i]))[0],
                      headings=cabecalho,
                      auto_size_columns=True, hide_vertical_scroll=True,
                      font=ft, num_rows=4,
                      justification='left')],
            [sg.Text(textos_grupo(*(lg[i]))[1], size=(30, 18),
                     justification='center', font=ft),
             sg.Text(textos_grupo(*(lg[i]))[2], size=(30, 18),
                     justification='center', font=ft),
             sg.Text(textos_grupo(*(lg[i]))[3], size=(30, 18),
                     justification='center', font=ft)],
            [sg.Button('Voltar'), sg.Text('      '), sg.Button('Oitavas')]
        ]
        janela.close()
        janela = sg.Window('Simulador de Copa do Mundo Beta V2.5',
                           layout, element_justification='c', size=tam)

    if eventos == 'Oitavas':
        j = 0
        topo2 = f'{lfas[j]}'
        layout = [
            [sg.Text(topo2,
                     font=ft)],
            [sg.Text(lf[j], size=(50, 22),
                     font=ft, justification='center')],
            [sg.Button('Voltar'), sg.Text('      '), sg.Button('Avançar')]
        ]
        janela.close()
        janela = sg.Window('Simulador de Copa do Mundo Beta V2.5',
                           layout, element_justification='c', size=tam)

    if eventos == 'Avançar':
        if j == 8:
            topo2 = 'Fim da Simulação! - Gustavo Albuquerque 10/2021'
            layout = [
                [sg.Text(topo2, size=(100, 2), justification='center',
                         font=ft)],
                [sg.Text("CHAVEAMENTO FINAL",
                         size=(100, 1), justification='center',
                         font=(ft, 30))],
                [sg.Text(paises_oitavas[0] + " X " + paises_oitavas[1] + " / " +
                         paises_oitavas[2] + " X " + paises_oitavas[3] + " / " +
                         paises_oitavas[4] + " X " + paises_oitavas[5] + " / " +
                         paises_oitavas[6] + " X " + paises_oitavas[7],
                         size=(100, 1), justification='center',
                         font=ft)],
                [sg.Text(paises_quartas[0] + " X " + paises_quartas[1] + " / " +
                         paises_quartas[2] + " X " + paises_quartas[3],
                         size=(100, 1), justification='center',
                         font=ft)],
                [sg.Text(paises_semi[0] + " X " + paises_semi[1],
                         size=(100, 1), justification='center',
                         font=ft)],
                [sg.Text("______________________________________________________",
                         size=(100, 1), justification='center',
                         font=ft, text_color="White")],
                [sg.Text("FINAL:",
                         size=(100, 1), justification='center',
                         font=ft, text_color="White")],
                [sg.Text(paises_final[0] + " X " + paises_final[1],
                         size=(100, 1), justification='center',
                         font=ft)],
                [sg.Text(copa[35][0] + " foi a seleção vencedora!",
                         size=(100, 1), justification='center',
                         font=(ft, 15), text_color="Gold")],
                [sg.Text("______________________________________________________",
                         size=(100, 1), justification='center',
                         font=ft, text_color="White")],
                [sg.Text("DECISÃO DE TERCEIRO LUGAR:",
                         size=(100, 1), justification='center',
                         font=ft, text_color="White")],
                [sg.Text(paises_terceiro[0] + " X " + paises_terceiro[1],
                         size=(100, 1), justification='center',
                         font=ft)],
                [sg.Text(copa[33][0] + " ficou na terceira colocacao!",
                         size=(100, 1), justification='center',
                         font=(ft, 15), text_color="Brown")],
                [sg.Text("______________________________________________________",
                         size=(100, 1), justification='center',
                         font=ft, text_color="White")],
                [sg.Text(paises_semi[2] + " X " + paises_semi[3],
                         size=(100, 1), justification='center',
                         font=ft)],
                [sg.Text(paises_quartas[4] + " X " + paises_quartas[5] + " / " +
                         paises_quartas[6] + " X " + paises_quartas[7],
                         size=(100, 1), justification='center',
                         font=ft)],    
                [sg.Text(paises_oitavas[8] + " X " + paises_oitavas[9] + " / " +
                         paises_oitavas[10] + " X " + paises_oitavas[11] + " / " +
                         paises_oitavas[12] + " X " + paises_oitavas[13] + " / " +
                         paises_oitavas[14] + " X " + paises_oitavas[15],
                         size=(100, 1), justification='center',
                         font=ft)],
                [sg.Text("",
                         size=(100, 1), justification='center',
                         font=ft, text_color="White")],
                [sg.Button('Voltar'), sg.Text('      '), sg.Button('Fim')]
            ]
            janela.close()
            janela = sg.Window('Simulador de Copa do Mundo Beta V2.5',
                               layout,
                               element_justification='c', size=tam)

        elif j == 7:
            art1 = []
            for item in Counter(autores_gols).items():
                art1.append([item[0], item[1]])

            art2 = sorted(art1, key=operator.itemgetter(1))
            art2[::-1]

            j = j + 1
            topo2 = f'{lfas[j]}'
            layout = [
                [sg.Text(topo2,
                         font=ft)],
                [sg.Text(lf[j], size=(50, 16),
                         font=ft, justification='center')],
                [sg.Text("_____________________", size=(50, 1),
                         font=ft, justification='center')],
                [sg.Text("ARTILHARIA", size=(65, 1),
                         font=(ft, 25), justification='center')],
                [sg.Text("", size=(50, 1),
                         font=ft, justification='center')],
                [sg.Table(art2[::-1],
                      headings=["Jogador", "Gols"],
                      auto_size_columns=True, hide_vertical_scroll=True,
                      font=ft, num_rows=4,
                      justification='left')],
                [sg.Text("", size=(50, 2),
                         font=ft, justification='center')],
            [sg.Button('Voltar'), sg.Text('      '), sg.Button('Avançar')]
            ]
            janela.close()
            janela = sg.Window('Simulador de Copa do Mundo Beta V2.5',
                               layout, element_justification='c', size=tam)
        
        else:
            j = j + 1
            topo2 = f'{lfas[j]}'
            layout = [
                [sg.Text(topo2,
                         font=ft)],
                [sg.Text(lf[j], size=(50, 22),
                         font=ft, justification='center')],
                [sg.Button('Voltar'), sg.Text('      '), sg.Button('Avançar')]
            ]
            janela.close()
            janela = sg.Window('Simulador de Copa do Mundo Beta V2.5',
                               layout, element_justification='c', size=tam)

    if eventos == 'Fim':
        janela.close()

print('Código por Gustavo Albuquerque - 10/2021')
