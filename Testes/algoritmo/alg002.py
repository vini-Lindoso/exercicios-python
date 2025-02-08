#2) creusa precisa comprar dolares

print('\033[1;44m-=' * 15 , '\033[m')
print('\033[1;44m Conversor de real para dollar\033[m')
print('\033[1;44m-=' * 15 , '\033[m')

reais = float(input('Quantos reais você que converte: '))
cotacao = 5.29
print('O valor equivalente a \033[1;32mR${:.2f}\033[m em dolares hoje é \033[1;32m${:.2f}'.format(reais, reais / cotacao))
