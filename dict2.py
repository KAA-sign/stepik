s = ('a aa abC aa ac abc bcd a').lower()
lst_s = [word for word in s.split()]
set_s = {word for word in lst_s}
cnt_word = {}
for set_word in set_s:
    cnt = 0
    for word in lst_s:
        if set_word == word:
            cnt += 1
    cnt_word[set_word] = cnt
for key in cnt_word.keys():
    print(key, cnt_word[key])