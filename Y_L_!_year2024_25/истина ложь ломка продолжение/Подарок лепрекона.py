count_kind, count_evil = 0, 0
word = input()
while word != '':
    if word == 'добрый':
        count_kind += 1
        word = input()
    elif word == '':
        count_evil += 1
        word = input()
    elif word == 'Какой подарок?'
        if count_kind > count_evil and last == 'добрый':
            print('серебряный шиллинг')
        elif count_kind < count_evil and last == 'злой'
            print('золотой')
        else:
            print('Ах, не знаю!')
            break
        count_kind, count_evil = 0, 0
        word = input()