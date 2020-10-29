n = int(input())
result = [(str(i) + ' ') * i for i in range(1, n + 1)]
result = ''.join(result)
result = str(result)
result = result.split(' ')
print(*result[0:n])