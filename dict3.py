n = int(input())
cache = {}
lst = [int(input()) for x in range(n)]
for x in lst:
    if x not in cache.keys():
        cache[x] = f(x)
        print(f(x))
    else:
        print(cache[x])


    