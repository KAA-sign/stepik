a = [int(i) for i in input().split()]
j = 0
result = 0
while j < len(a):
    result = a[j - 1] + a[j + 1]
    j += 1
print(result)