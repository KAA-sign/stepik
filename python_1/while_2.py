a = int(input())
b = int(input())
p = a * b
while a != 0 and b != 0 :
    if a > b:
        a = a % b
    else:
        b = b % a
    nod = a + b
    nok = p // nod
print(nok)