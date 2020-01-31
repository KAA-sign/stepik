a = [int(i) for i in input().split()]
a.sort()
result = []
i = 0
count = 0
while i < (len(a) - 1):
    if a[i] == a[i + 1]:
        count += 1
        if count > 0:
            result.extend([a[i]])
        count = 0
    i += 1
result = [str(i) for i in result]
print(' '.join(result))