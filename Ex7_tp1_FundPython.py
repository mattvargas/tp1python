# INSTITUTO INFNET RIO DE JANEIRO
# ALUNO: MATHEUS ANDRÉ DE LIMA VARGAS
# GRADUAÇÃO EM ENGENHARIA DA COMPUTAÇÃO
# TESTE DE PERFORMANCE I PYTHON
# PROF.: THAIS VIANA
# EXERCÍCIO 7

import os
p = input( "Digite o arquivo ou pasta:  ")
if os.path.isfile(p):
 print(p, 'é um diretório!')
else:
 print(os.path.basename(p))