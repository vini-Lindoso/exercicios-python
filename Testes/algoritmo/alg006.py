print('\033[1;44m-' * 30, '\033[m')
print('\033[1;44m{:^31}\033[m'.format('DEPARTENTO DE TRANSITO'))
print('\033[1;44m-' * 30, '\033[m')
idade = int(input('Qual a sua idade:'))
if idade >= 18:
    situ = 'apto'
else:
    situ = 'inapto'
print('\033[1;44m-' * 30, '\033[m')
print('\033[1;44m{:^30}'.format('Você está'),'\033[m')
print('\033[1;44m{:^31}\033[m'.format('{} para dirigir'.format(situ)))
print('\033[1;44m-' * 30, '\033[m')