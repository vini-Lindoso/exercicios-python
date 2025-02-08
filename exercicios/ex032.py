year = int(input('Type it a year to find out if it is a leap year: '))
if year % 4 and year % 100 != 0 or year % 400 == 0:
	answer = 'is'
else:
	answer = 'is not'
print('{} {} a leap year.'.format(year, answer))