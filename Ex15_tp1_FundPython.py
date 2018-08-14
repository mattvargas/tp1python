# INSTITUTO INFNET RIO DE JANEIRO
# ALUNO: MATHEUS ANDRÉ DE LIMA VARGAS
# GRADUAÇÃO EM ENGENHARIA DA COMPUTAÇÃO
# TESTE DE PERFORMANCE I PYTHON
# PROF.: THAIS VIANA
# EXERCÍCIO 15

import subprocess
import psutil
import time

p = subprocess.Popen("calc")
r = psutil.pids()
psutil.process_iter()
p = psutil.Process(p.pid)
print(p.name())
print(p.username())
print(p)