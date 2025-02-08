import random
v = random.randint(0 , 5)
print('-=-' * 20)
print('Guess what number I`m thinking of...')
print('-=-' * 20)
n = int(input('try a number between 0 and 5: '))
if v == n:
    print('Congratulation!! you´re right!!\nthe number that I was thinking of is {}'.format(v))
else:
    print('You missed!!\nThe number that I was thinking of is {}'.format(v))