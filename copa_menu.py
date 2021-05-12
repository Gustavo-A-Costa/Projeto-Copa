# Código por Gustavo Albuquerque - 05/05/2021
from PySimpleGUI import PySimpleGUI as sg
from sorteio import sorteio_copa, texto_sorteio
from v2_simulador_grupos import tabela_grupos, textos_grupo
from v2_matamata import copa_mundo, textos_matamata

# fonte
ft = 'Bahnschrift'

# tamanho da janela
tam = (800, 450)

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

# layout
sg.theme('Dark Brown 1')
menu_principal = [
                 [sg.Text('Simulador de Copa do Mundo (Iniciante)',
                          size=(100, 5),
                          justification='center', font=ft)],
                 [sg.Text('V2.3 / Gustavo Albuquerque 11/05/2021',
                          size=(100, 5),
                          justification='center', font=ft)],
                 [sg.Button('Começar!')],
]

layout = menu_principal
# janela
janela = sg.Window('Simulador de Copa do Mundo V2.3', layout,
                   element_justification='c', size=tam)
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
        janela.close()
        janela = sg.Window('Simulador de Copa do Mundo Beta V2.3',
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
            [sg.Text(textos_grupo(*(lg[i]))[1],
                     justification='center', font=ft),
             sg.Text(textos_grupo(*(lg[i]))[2],
                     justification='center', font=ft),
             sg.Text(textos_grupo(*(lg[i]))[3],
                     justification='center', font=ft)],
            [sg.Button('Próximo')]
        ]
        janela.close()
        janela = sg.Window('Simulador de Copa do Mundo Beta V2.3',
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
            [sg.Text(textos_grupo(*(lg[i]))[1],
                     justification='center', font=ft),
             sg.Text(textos_grupo(*(lg[i]))[2],
                     justification='center', font=ft),
             sg.Text(textos_grupo(*(lg[i]))[3],
                     justification='center', font=ft)],
            [sg.Button('Voltar'), sg.Text('      '), sg.Button('Próximo')]
        ]
        janela.close()
        janela = sg.Window('Simulador de Copa do Mundo Beta V2.3',
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
                [sg.Text(textos_grupo(*(lg[i]))[1],
                         justification='center', font=ft),
                 sg.Text(textos_grupo(*(lg[i]))[2],
                         justification='center', font=ft),
                 sg.Text(textos_grupo(*(lg[i]))[3],
                         justification='center', font=ft)],
                [sg.Button('Voltar'), sg.Text('      '), sg.Button('Próximo')]
            ]
            janela.close()
            janela = sg.Window('Simulador de Copa do Mundo Beta V2.3',
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
            [sg.Text(textos_grupo(*(lg[i]))[1],
                     justification='center', font=ft),
             sg.Text(textos_grupo(*(lg[i]))[2],
                     justification='center', font=ft),
             sg.Text(textos_grupo(*(lg[i]))[3],
                     justification='center', font=ft)],
            [sg.Button('Voltar'), sg.Text('      '), sg.Button('Oitavas')]
        ]
        janela.close()
        janela = sg.Window('Simulador de Copa do Mundo Beta V2.3',
                           layout, element_justification='c', size=tam)

    if eventos == 'Oitavas':
        j = 0
        topo2 = f'{lfas[j]}'
        layout = [
            [sg.Text(topo2,
                     font=ft)],
            [sg.Text(lf[j],
                     font=ft, justification='center')],
            [sg.Button('Voltar'), sg.Text('      '), sg.Button('Avançar')]
        ]
        janela.close()
        janela = sg.Window('Simulador de Copa do Mundo Beta V2.3',
                           layout, element_justification='c', size=tam)

    if eventos == 'Avançar':
        if j == 8:
            topo2 = 'Fim da Simulação! - Gustavo Albuquerque 11/05/2021'
            layout = [
                [sg.Text(topo2, justification='center',
                         font=ft)],

                [sg.Button('Voltar'), sg.Text('      '), sg.Button('Fim')]
            ]
            janela.close()
            janela = sg.Window('Simulador de Copa do Mundo Beta V2.3',
                               layout,
                               element_justification='c', size=(500, 500))
        else:
            j = j + 1
            topo2 = f'{lfas[j]}'
            layout = [
                [sg.Text(topo2,
                         font=ft)],
                [sg.Text(lf[j],
                         font=ft, justification='center')],
                [sg.Button('Voltar'), sg.Text('      '), sg.Button('Avançar')]
            ]
            janela.close()
            janela = sg.Window('Simulador de Copa do Mundo Beta V2.3',
                               layout, element_justification='c', size=tam)

    if eventos == 'Fim':
        janela.close()

print('Código por Gustavo Albuquerque - 06/05/2021')
