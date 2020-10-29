summ = 0
result = 0
while True:
    i = int(input())
    summ += i
    result += i ** 2
    if summ == 0:
        print(result)
        break
print()