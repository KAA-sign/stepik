s = 'a aa abC aa ac abc bcd a'
s = s.lower()
x = ''
cnt = 0
word_list = [word for word in s.split()]
for word in word_list:
    if word == x:
        cnt += 1
        x = word

