# with open ('in.txt') as file_in, open("out.txt", 'w') as file_out:
#     for line in file_in:

s = ('abc a bCd bC AbC BC BCD bcd ABC').lower()
lst_s = [word for word in s.split()]
set_s = {word for word in lst_s}
cnt_word = {}
for set_word in set_s:
    cnt = 0
    for word in lst_s:
        if set_word == word:
            cnt += 1
    cnt_word[set_word] = cnt
print(max(cnt_word, key=cnt_word.get), velue)