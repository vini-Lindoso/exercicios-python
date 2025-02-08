#4)Creusa pegou um emprestimo com 20% de juros
emprestimo = float(input('O emprestimo foi no valor de: '))
parcelas = int(input('Em quantas parcelas: '))
vemp = emprestimo * 1.20
vpar = vemp / parcelas
from time import sleep
print('-=' * 10, '\n{:^20}'.format('CALCULANDO'),'\n', '-=' * 10)
sleep(2)
print('O emprestimo ficara no valor de R${:.2f}, sera pago em {} parcelas de R${:.2f}'.format(vemp, parcelas, vpar))