a = [int(i) for i in input().split()]
result = []
if len(a) != 1:
    result = [a[j - 1] + a[j + 1] for j in range(len(a) - 1)]
    result.extend([a[-2] + a[0]])
    result = [str(i) for i in result]
    print(' '.join(result))
else:
    print(' '.join([str(i) for i in a]))