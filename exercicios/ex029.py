m = 80
v = int(input('What speed was the car in Km/h: '))
if v <= m:
	print('The speed limit on the road is {}Km/h,\nYour car is bellow speed limit, at {}Km/h...\nYou will not be fined.'.format(m , v))
else:
	print('The speed limit on the road is {}Km/h,\nYour car is above speed limit, at {}Km/h...\n -You will be fined, in the amount of R${:.2f}.'.format(m , v , (v - m) * 7))
