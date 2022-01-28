# создаем список слов
words = ['python', 'c++', 'c', 'scala', 'java']

# создаем функцию для выбора букв со списком слов и буквами в них
def count_letter (words, letter):
	# обозначаем выборку с первой буквы - это 0
	count=0
	for word in words:
		if letter in word:
			count += 1
	return count

letter='a'
print (count_letter (words, letter))