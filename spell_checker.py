d = int(input('Enter number of known words: '))
# d = 4
known_words = [input().lower() for i in range(d)]
# known_words = ['champions', 'we', 'are', 'stepik']
l = int(input('Enter number of rows: '))
# l = 3
lines_to_check = [input().lower().split() for i in range(l)]
# lines_to_check = [['we', 'are', 'the', 'champignons'], ['we', 'are', 'the', 'champions'], ['stepic']]


def gen_word_list(lstlst):
    word_to_check = []
    for lst in lstlst:
      word_to_check.extend(lst)
    return word_to_check

def spell_check(lstt, known_words):
    result = list(set(lstt) - set(known_words))
    return result
# result=list(set(word_to_check) ^ set(known_words))


wtc = gen_word_list(lines_to_check)
rt = spell_check(wtc, known_words)
print(*rt, sep='\n')