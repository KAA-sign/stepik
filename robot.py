n = int(input())
if n == 1 or (n < 100 and n % 10 == 1 and n % 11 != 0) or (n > 100 and n % 10 == 1 and n % 100 != 11):
    print(n, 'программист')
elif 2 <= n <= 4 or (n != 12 and n % 10 == 2 and n % 100 != 12) or (n != 13 and n % 10 == 3 and n % 100 != 13) or (n != 14 and n % 10 == 4 and n % 100 != 14):
    print(n, 'программиста')
else:
    print(n, 'программистов')