n, k = map(int, input().split())
def comb(n, k):
    if k == 0 or k > n or n == k:
        return 1
    else:
        return comb(n - 1, k) + comb(n - 1, k - 1)


print(comb(n, k))