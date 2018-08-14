# Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB,
#quanto de memória principal e quanto de memória de paginação (swap) existem no
#computador.


import psutil


disco = psutil.swap_memory()
hd = round(disco.total/(1024*1024), 2)
print(hd, "GB")
  
  