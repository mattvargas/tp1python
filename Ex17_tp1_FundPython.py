# INSTITUTO INFNET RIO DE JANEIRO
# ALUNO: MATHEUS ANDRÉ DE LIMA VARGAS
# GRADUAÇÃO EM ENGENHARIA DA COMPUTAÇÃO
# TESTE DE PERFORMANCE I PYTHON
# PROF.: THAIS VIANA
# EXERCÍCIO 17

import psutil
import time

for i in range(20):
    time.sleep(0.1)
    print(psutil.cpu_times_percent())