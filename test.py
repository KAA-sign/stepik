import random
while True:
    words = {
    'На свете есть много лягушек: все они очень разные. \
    Свои названия они получили за свою внешность: живёт в \
    траве - травяная, с острой мордой - остромордая, живёт в пруду - прудовая.\
    А эта африканская лягушка получила своё название за необычный рот.\
    Как зовут эту лягушку?':'узкорот',
    ' Эта птица может ходить по дну водоёма, похожа на воробья. Её так и прозвали\
    «водяной воробей». Что это за птица?':'оляпка',
    'На морском дне растёт очень опасная водоросль: актиния – она больно жжётся. \
    А эта рыбка дружит с ней. И наряд у этой рыбки яркий, весёлый, пёстрый. \
    Что это за рыбка?':'клоун'
    }
    question, word = random.choice(list(words.items()))
    print('Задание: ', question)
    skr=len(word)*'*'
    print(skr)
    while '*' in skr:
        letter_or_word=input('Введите букву или слово: ')
        if letter_or_word!=word:
            letter=""
            for index in range(len(word)):
                if letter_or_word==word[index]:
                    letter+=letter_or_word
                elif letter_or_word!=word[index]:
                    letter+=skr[index]
            skr=letter
            print(skr)
        elif letter_or_word==word:
            print('Вы угадали слово:')
            break
    exit=str(input('Хотите ли вы продолжить игру? Y/N:'))
    if exit=='Y': 
        True
    elif exit=='N':
        break