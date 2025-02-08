city = str(input('Type it the name a city, please: ')).strip()
n = city[:6]
n2 = n.upper()
print('the name of chosen city is {} and a statement that the start with "Santo" is {}'.format(city.title(), 'SANTO' in n2))
