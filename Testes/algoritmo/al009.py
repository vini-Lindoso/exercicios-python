n = int(input('digite um numero para ver a tabuada dele:'))
cont = n
while cont < 11:
    r = cont * n
    print(n, ' x ', cont, '= {}'.format(r))
    cont += 1
print('fim')
