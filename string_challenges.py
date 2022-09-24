# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(*map(word.lower().count, "уеыаоэёяию"))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(' \n'.join([x[0] for x in sentence.split()]))


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(sum([len(x) for x in sentence.split()])/len([len(x) for x in sentence.split()]))