a = float(input('qual a Altura da Parede em Metros? '))
l = float(input('qual a Largura da parede em metros? '))
area = a * l
print('A parede possui uma área de {:.2f} metros e você necessitara de {:.2f} litros de tinta'.format(area, (area/2)))