# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???

print(sum([len(x) for x in sentence.split()])/len([len(x) for x in sentence.split()]))