import os
 
p = input(" Digite o arquivo : ")
if os.path.isfile(p):
 print(p, 'é um arquivo!')
else:
 print(p, 'não é um arquivo!')
  