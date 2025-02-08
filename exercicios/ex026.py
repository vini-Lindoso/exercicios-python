text = str(input('type it a text: ')).strip()
print('in te text there are {} letter "A".'.format(text.upper().count('A')))
print('the fist time position that a letter "A" is in {}'.format(text.upper().find('A')+1))
text2 = text[::-1]
n = len(text) - text2.upper().find('A')
print('the last time position that a letter "A" is in {}'.format(n))