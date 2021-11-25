star = int(input("введите количество звездочек: "))
for i in range(star , 0 , -1 ):
	for n in range(i - 1):
		print('*', end=' ')
	print()
