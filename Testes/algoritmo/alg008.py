print('\033[1;32m--------------------------\033[m')
print('\033[1;32mClassificação de uma aluno\033[m')
print('\033[1;32m--------------------------\033[m')
media = int(input('Qual a media de nota do aluno: '))
if media > 900:
    digite = '\033[1;34m A\33[m, parabens!'
else:
    if media >= 800:
        digite ='\033[1;32m B\033[m.'
    else:
        if media >= 700:
            digite = '\033[1;33m C\033[m.'
        else:
            if media >= 600:
                digite = '\033[1;33m D\033[m. Por pouco, estude mais'
            else:
                if media >= 500:
                    digite = '\033[1;31m E\033[m.Estude mais!'
                else:
                    digite = '\033[1;33m F\033[m.Voce foi muito mal, precisa estudar muito'
print('Com uma media {} sua classificação é {}'.format(media, digite))