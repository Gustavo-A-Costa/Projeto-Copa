# Código por Gustavo Albuquerque - 20/04/2021
from matamata import copa_mundo
import sys

sys.stdout = open("Copa do Mundo.txt", "w")

copa_mundo()
print('Código por Gustavo Albuquerque - 20/04/2021')

sys.stdout.close()
