print('selecione um idioma/select language:')
language = int(input('digite 1 para portugues / Type it another number from English\n language: '))
if language == 1:
    number = int(input('digite um numreo inteiro qualquer: '))
    v = number % 2
    if v == 0:
        print('O número {} é PAR'.format(number))
    else:
        print('O numero {} é IMPAR'.format(number))
    print('Obrigado!')
else:
    number = int(input('Tipe it a number integer: '))
    v = number % 2
    if v == 0:
        print('The number {} is even'.format(number))
    else:
        print('The number {} is odd'.format(number))
    print('Thank you!')