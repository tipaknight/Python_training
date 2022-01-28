import random

yes = "да"
no = "нет"

while True:
	num = random.randint(1, 10)
	guess = int(input ('Введите число от 1 до 10:'))
	if guess == num:
		print('Угадали', 'До свидания!')
		break
	elif guess > 10:
		print('Число не может быть больше 10')
	elif guess < 1:
		print('Число не может быть меньше 1')

	else:
		print('Неправильно, было загадано число: ' + str(num))
	guess_1 = str(input('Хотите продолжите? Введите "да" или "нет": '))
	if guess_1 == yes:
		guess == guess_1
	elif guess_1 == no:
		print('До свидания')
		break
