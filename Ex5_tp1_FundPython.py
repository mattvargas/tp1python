import os
import psutil

p = input(" Digite o diretorio : ")
if os.path.exists(p):
 print(p, 'existe!')
else:
 print(p, 'não existe!')