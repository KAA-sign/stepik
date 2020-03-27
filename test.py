lst = [1, 2, 3, 4, 5, 6]
for i in lst:
    if  i % 2 != 0: 
        lst.remove(i) 
        for i in lst:
            lst.append(i // 2)