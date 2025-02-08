i = str(input('''Language / IdiomaPortugues
[P]Portugues
[E]English
opção: '''))
lang = i.upper()
if lang == 'P':
    v = int(input('Digite um numero inteiro qualquer: '))
    print('''Qual base deseja?
    [1]Binario
    [2]Octal
    [3]Hexadecimal''')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        r = bin(v)
        s = str(r)
        print('A representação binaria do Valor de {} é \033[1;34m{}\033[m'.format(v, s[2:]))
    elif opcao == 2:
        r = oct(v)
        s = str(r)
        print('A representação octal do Valor de {} é \033[1;34m{}\033[m'.format(v, s[2:]))
    elif opcao == 3:
        r = hex(v)
        s = str(r)
        print('A representação hexadecimal do Valor de {} é \033[1;34m{}\033[m'.format(v, s[2:]))
    else:
        print('\033[1;31mErro!\033[m Base desconhecida.')
    print('--------------------')
    print('   Muito obrigado   ')
elif lang == 'E':
    v = int(input('Type it a number: '))
    print('''which base do you went?
     [1]binary
     [2]Octal
     [3]Hexadecimal
     ''')
    opcao = int(input('Base Code: '))
    if opcao == 1:
        r = bin(v)
        s = str(r)
        print('The Binary Representation of {} number is \033[1;34m{}\033[m'.format(v, s[2:]))
    elif opcao == 2:
        r = oct(v)
        s = str(r)
        print('The Octal Representation of {}number is \033[1;34m{}\033[m'.format(v, s[2:]))
    elif opcao == 3:
        r = hex(v)
        s = str(r)
        print('The Hexadecimal representation of {} number is \033[1;34m{}\033[m'.format(v, s[2:]))
    else:
        print('\033[1;31mError!\033[m Unknown base.')
    print('--------------------')
    print('     Thank you      ')
else:
    print('\033[1;31mError!\033[m Unknown language.')
    print('\033[1;31mErro!\033[m Idioma desconhecido.')
