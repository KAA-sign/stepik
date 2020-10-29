def modify_list(lst):
    new_lst = []
    for i in  reversed(lst):
        if  i % 2 != 0: 
            lst.remove(i)
    for i in lst:
        new_lst.append(i // 2)
    lst[:] = new_lst
    
    
modify_list([1, 2, 3, 4, 5, 6])