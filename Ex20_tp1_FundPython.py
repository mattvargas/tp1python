#Escreva um programa em Python usando o módulo ‘psutil’,
#que imprima para a partição corrente:

import psutil
#A : nome do dispositivo
disco = psutil.disk_partitions()
print(disco.sdiskpart)