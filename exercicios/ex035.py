print('\033[34;40m-=' * 10 , '\033[m')
print('\033[33;40m Analysing triangle  \033[m')
print('\033[34;40m-=' * 10 , '\033[m')
r1 = float(input('length of first line: '))
r2 = float(input('length of second line: '))
r3 = float(input('length of last line: '))
list_1 = [r1, r2, r3]
order = sorted(list_1)
if order[2] < order[0] + order[1]:
    triangle = '\033[1;32mYes, it´s possible\033[m'
else:
    triangle = '\033[1;31mNo, it´s not possible\033[m '
print('{}to make a triangle with the measurements {}cm, {}cm and {}cm.'.format(triangle, r1, r2 ,r3 ))