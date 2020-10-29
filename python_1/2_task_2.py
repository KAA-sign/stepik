a = [int(i) for i in input().split()]
#a = [5, 8, 2, 7, 8, 8, 2, 4]
n = int(input())
result = []
i = 0
if n in a:
    cnt = a.count(n)
    while True:
        i = a.index(n, i)
        result.append(i)
        if len(result) == cnt:
            print(*result)
            break
        i += 1
else:
    print('Отсутствует')