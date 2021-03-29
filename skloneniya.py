import pymorphy2

morph = pymorphy2.MorphAnalyzer()
word = morph.parse(input())[0]

if 'NOUN' in word.tag.POS:
    print('Единственное число:')
    print('Именительный падеж:', word.inflect({'nomn'}).word)
    print('Родительный падеж:', word.inflect({'gent'}).word)
    print('Дательный падеж:', word.inflect({'datv'}).word)
    print('Винительный падеж:', word.inflect({'accs'}).word)
    print('Творительный падеж:', word.inflect({'ablt'}).word)
    print('Предложный падеж:', word.inflect({'loct'}).word)
    print('Множественное число:')
    print('Именительный падеж:', word.inflect({'nomn', 'plur'}).word)
    print('Родительный падеж:', word.inflect({'gent', 'plur'}).word)
    print('Дательный падеж:', word.inflect({'datv', 'plur'}).word)
    print('Винительный падеж:', word.inflect({'accs', 'plur'}).word)
    print('Творительный падеж:', word.inflect({'ablt', 'plur'}).word)
    print('Предложный падеж:', word.inflect({'loct', 'plur'}).word)
else:
    print('Не существительное')
