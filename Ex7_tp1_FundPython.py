import os
p = input( "Digite o arquivo ou pasta:  ")
if os.path.isfile(p):
 print(p, 'é um diretório!')
else:
 print(os.path.basename(p))