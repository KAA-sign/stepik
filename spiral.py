n = int(input())
A = [[0 for j in range(n)] for i in range(n)]
count = 1
for i in range(n):
    for j in range(n):
        while count < (n ** 2):
            A[i][j] = count
            count += 1
    for j in range(n):
        for i in range(n):
            A[i][j] = count
            count += 1

for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()