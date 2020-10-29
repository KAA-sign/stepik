a = 7
b = 10
c = 5
d = 6
for j in range(c, d+1):
    print('\t', j, end='')
print()
for i in range(a, b+1):
    print(i, '\t', end='')
    for j in range(c, d + 1):
        print(i * j, '\t', end='')
    print()
print()