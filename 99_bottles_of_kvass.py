import pymorphy2

i = 99
w = pymorphy2.MorphAnalyzer().parse('бутылка')[0]

while i:
    print(f'В холодильнике {i} {w.make_agree_with_number(i).word} кваса.\n'
          f'Возьмём одну и выпьем.')
    i -= 1

    if i % 10 == 1 and i != 11:
        o = 'Осталась'
    else:
        o = 'Осталось'

    print(f'{o} {i} {w.make_agree_with_number(i).word} кваса.')
