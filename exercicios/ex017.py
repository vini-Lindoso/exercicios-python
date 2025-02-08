'''co = float(input('valor do cateto oposto: '))
ca = float(input('valor do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('a hipotenusa será {:.2f}'.format(h))'''

import math
co = float(input('valor do cateto oposto: '))
ca = float(input('valor do cateto adjacente: '))
hi = math.hypot( co , ca)
print('O valor da hipotenusa sera {:.2f}' .format(hi))

