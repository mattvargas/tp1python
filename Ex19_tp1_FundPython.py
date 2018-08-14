#Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto
#de armazenamento disponível há na partição do sistema (onde o sistema está instalado).

import psutil


disco = psutil.disk_usage(path='C:')
print(disco.total)

