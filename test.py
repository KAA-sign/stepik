n = int(input())
cache = {}
lst = [int(input()) for x in range(n)]
for x in lst:
    if x not in cache:
        cache[x] = f(x)
        print(f(x))
    else:
        print(f(x))