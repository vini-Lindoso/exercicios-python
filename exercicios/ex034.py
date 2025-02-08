print('\033[1;44m-=' * 20,'\033[m')
print('\033[1;44m{:^40} \033[m'.format('Salary machine'))
print('\033[1;44m-=' * 20,'\033[m')
si = float(input('\033[7;40;33mwhat a salary of employee: \033[m'))
if si > 1250:
    increase = 0.10
else:
    increase = 0.15
print('\033[44mthe employee`s increase will be {}R${:.2f}{} \033[m\n\033[44mand he start will receive:     {}R${:.2f}{}\033[m'.format('\033[30;4m', si * increase, '\033[m' , '\033[30;4m' , si * (increase + 1), '\033[m'))