l = str(input('English [E]\nPortuguês [P]\nTipe it here/ Digite Aqui: ')).strip()
if l.upper() == 'E':
    print('\033[1;45m-=-' * 12, '\033[m')
    print('\033[1;45m{:^37}\033[m'.format('Calculator of Finance!'))
    print('\033[1;45m-=-' * 12, '\033[m')
    price = float(input('Type it the price of property: R$'))
    salary = float(input('Type it your salary: R$ '))
    year = int(input('Type it in how many installments: '))
    installments = year * 12
    p = price / installments
    if p > (salary * 0.30):
        print('Your finance will be \033[1;31mDisapproved!\033[m\nReason: \033[1;31m Price of Installments {} Greater than 30% of your income.\033[m'.format(p))
    else:
        print(
            'Your finance will be \033[1;32mApprovad!\033[m \n You will pay {} installments in the price of R${:.2f}.'.format(
                installments, p))
    print('--------------------')
    print('\033[1m{:^20}'.format('Thank you!'))
    print('--------------------')
elif l.upper() == 'P':
    print('\033[1;45m-=-' * 12,'\033[m')
    print('\033[1;45m{:^37}\033[m'.format('Calcauladora de financiamentos!'))
    print('\033[1;45m-=-' * 12,'\033[m')
    price = float(input('Qual o preço do imóvel: R$'))
    salary = float(input('Digite o seu salar: R$'))
    year = int(input('Digite a quantidade de parcelas: '))
    installments = year * 12
    p = price / installments
    if p > (salary * 0.30):
        print(
            'O Seu financiamento será \033[1;31mreprovado!\033[m\nMotivo: \033[1;31m Valor da parcela {} acima de 30% da renda\033[m'.format(
                p))
    else:
        print(
            'O seu financiamento será \033[1;32maprovado!\033[m \nE você pagara {} parcelas no valor de R${:.2f}.'.format(
                installments, p))
    print('--------------------')
    print('\033[1m{:^20}'.format('Obrigado!'))
    print('--------------------')
else:
    print('Error!Language not found! / Erro! Idioma não encontrado!')