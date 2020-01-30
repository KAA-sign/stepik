s = input()
i = 0
cnt = 1
while i < len(s):
    if s[i] == s[i+1]:
        cnt += 1
    elif s[i] != s[i+1] or i < (len(s) - 1):
        print(s[i], cnt, end='')
        cnt = 1
    i += 1
print()