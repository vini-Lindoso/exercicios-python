name = str(input('Type a full name: ')).strip().title()
list_1 = name.split(' ')
esp = name.count(' ')
print('Nice to meet you!! \nYour first name is {} \nYour last name is {}'.format(list_1[0], list_1[esp]))