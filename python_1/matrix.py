A = []
inp = input()
intermediate = []
result = []
count = 0
while inp != 'end':# Ввод матрицы
    row = [int(i) for i in inp.split()]
    A.append(row)
    inp = input()
for i in range(0, len(A)):# len(A) это кол-во столбцов
    for j in range(0, len(row)):
        intermediate.append(A[i - 1][j] + A[i - len(A) + 1][j] + A[i][j - 1] + (A[i][j - len(row) + 1]))
        count += 1
        if count == len(row):
            result.append(intermediate)
            count = 0
            intermediate = []
for i in range(0, len(A)):
    for j in range(0, len(row)):
        print(result[i][j], end=' ')
    print()