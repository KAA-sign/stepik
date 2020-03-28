lst = [1, 3, 5, 7]
new_lst = []
for i in reversed(lst):
    if  i % 2 != 0: 
        lst.remove(i)
for i in lst:
    new_lst.append(i // 2)
lst[:] = new_lst