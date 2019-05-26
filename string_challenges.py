# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'

letter_finder = word.lower()
print(letter_finder.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'

letter_finder = word.lower()
vowel = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
count = 0
for letters in vowel:
    count += letter_finder.count(letters)
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

words_count = sentence.split(' ')
print(len(words_count))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

words_count = sentence.split(' ')
for letters in words_count:
    print(letters[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'

words_count = sentence.split()
count_len = 0
for letters in words_count:
    count_len += len(letters)
print(count_len / len(words_count))