import math
ang = float(input('Angulo desejado: '))
r = math.radians(ang)
c = math.cos(r)
s = math.sin(r)
t = math.tan(r)
print('O angulo de {}º possui um seno de {:.4f}, cosseno de {:.4f} e tangente {:.4f}'.format( ang , s , c , t))
