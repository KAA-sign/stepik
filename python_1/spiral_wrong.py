n = int(input())
A = [[0 for j in range(n)] for i in range(n)]
i = 0
count = 0
while count < (n ** 2):
    if i == 0:
        for j in range(n):
            count += 1
            A[i][j] = count
        if j == n - 1:
            for i in range(1, n):
                count += 1
                A[i][j] = count
    if i == n - 1:
        for j in range(n-2, -1, -1):
            count += 1
            A[i][j] = count
    if j == 0:
        for i in range(n-2, 0, -1):
            count += 1
            A[i][j] = count
    if i == 1:
        for j in range(1, n-1):
            count += 1
            A[i][j] = count
    if j == n - 2:
        for i in range(2, n-1):
            count += 1
            A[i][j] = count
    if i == n - 2:
        for j in range(n-3, 0, -1):
            count += 1
            A[i][j] = count
    if j == 1:
        for i in range(n-3, 1, -1):
            count += 1
            A[i][j] = count
    if i == 2:
        for j in range(2, n-2):
            count += 1
            A[i][j] = count

    if j == n - 3:
        for i in range(n-3, 2, -1):
            count += 1
            A[i][j] = count

    if i == n - 3:
        for j in range(n-4, 1, -1):
            count += 1
            A[i][j] = count


for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()


# n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин
# a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1  # расставляем мины
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     # (ai, aj)
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# # вывод результата
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()

