text = open("in.txt", 'r')
lst_s = text.read().replace('\n', ' ').lower().split()
text.close()
# lst_s = [word for word in s.lower().split()]
set_s = {word for word in lst_s}
cnt_word = {}
for set_word in set_s:
    cnt = 0
    for word in lst_s:
        if set_word == word:
            cnt += 1
    cnt_word[set_word] = cnt
v=list(cnt_word.values())
k=list(cnt_word.keys())
print(k[v.index(max(v))], max(v))