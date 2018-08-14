# INSTITUTO INFNET RIO DE JANEIRO
# ALUNO: MATHEUS ANDRÉ DE LIMA VARGAS
# GRADUAÇÃO EM ENGENHARIA DA COMPUTAÇÃO
# TESTE DE PERFORMANCE I PYTHON
# PROF.: THAIS VIANA
# EXERCÍCIO 5

import os
import psutil

p = input(" Digite o diretorio : ")
if os.path.exists(p):
 print(p, 'existe!')
else:
 print(p, 'não existe!')