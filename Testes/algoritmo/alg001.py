#Creusa
#1)quantos anos creusa tem:
import datetime
from time import sleep
hoje = str(datetime.date.today())
hoje2 = hoje.split('-')
esse_ano = int(hoje2[0])
nasc = int(input('\033[4;31mEm que ano você nasceu?\033[m '))
idade = esse_ano - nasc
print('\033[1;34mComo você nasceu em {} e estamos em {}, você está fazendo {} anos '.format(nasc, esse_ano, idade))
sleep(2)
