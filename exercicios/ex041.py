anon = int(input('Em que a no o aluno nasceu: '))
import datetime
anoh = datetime.date.today().year
idade = anoh - anon
print('Uma pessoa que nasceu em {} atualmente está com {} anos de idade'.format(anon, idade))
if 0 < idade < 9:
	cat = 'MIRIM'
elif 9 <= idade < 14:
	cat = 'INFANTIL'
elif 14 <= idade < 19:
    cat = 'JÚNIOR'
elif 19 <= idade < 25:
	cat = 'SÊNIOR'
elif idade >= 25:
	cat = 'MASTER'
else:
	cat = 'ERRO!'
print('E deve competir como {}'.format(cat))