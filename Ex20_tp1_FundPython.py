# INSTITUTO INFNET RIO DE JANEIRO
# ALUNO: MATHEUS ANDRÉ DE LIMA VARGAS
# GRADUAÇÃO EM ENGENHARIA DA COMPUTAÇÃO
# TESTE DE PERFORMANCE I PYTHON
# PROF.: THAIS VIANA
# EXERCÍCIO 20

import psutil
#A : nome do dispositivo
disco = psutil.disk_partitions()
print(disco.sdiskpart)