# INSTITUTO INFNET RIO DE JANEIRO
# ALUNO: MATHEUS ANDRÉ DE LIMA VARGAS
# GRADUAÇÃO EM ENGENHARIA DA COMPUTAÇÃO
# TESTE DE PERFORMANCE I PYTHON
# PROF.: THAIS VIANA
# EXERCÍCIO 8

import os
p = input( "Digite o arquivo ou pasta:  ")
status = os.stat(p)
if os.path.isfile(p):
 print(p, 'é um arquivo!')
 print(status.st_size)
else:
 print("não é um arquivo")