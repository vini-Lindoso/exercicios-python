distance = float(input('What is the distance of the travel in Km: '))
if distance > 200:
    print('The ticket for a travel of {:.1f}Km will cost R${:.2f}.'.format(distance, distance * 0.45))
else:
    print('The ticket for a travel of {:.1f}Km will cost R${:.2f}.'.format(distance, distance * 0.50))