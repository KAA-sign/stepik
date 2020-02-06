n = int(input())
A = []
count = 0
for i in range(n):
    for j in range(n):
        intermediate.append(A[i][j])
        count += 1
        if count == n:
            result.append(intermediate)
            count = 0
            intermediate = []