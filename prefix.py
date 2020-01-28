s = input()
i = 0
cnt = 1
while i < len(s):
    if s[i] == s[i+1]:
        cnt += 1
    else:
        print(i, count, end='')
print()