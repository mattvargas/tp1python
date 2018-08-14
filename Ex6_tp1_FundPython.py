# INSTITUTO INFNET RIO DE JANEIRO
# ALUNO: MATHEUS ANDRÉ DE LIMA VARGAS
# GRADUAÇÃO EM ENGENHARIA DA COMPUTAÇÃO
# TESTE DE PERFORMANCE I PYTHON
# PROF.: THAIS VIANA
# EXERCÍCIO 6

import os

p = input(" Digite o arquivo : ")
if os.path.isfile(p):
    print(p, 'é um arquivo!')
else:
    print(p, 'não é um arquivo!')
