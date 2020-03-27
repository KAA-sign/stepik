

def modify_list(lst):
    new_list = []
    for i in lst:
        if  i % 2 != 0: 
            lst.remove(i) 
            lst.append(i // 2)

    modify_list([1, 2, 3, 4, 5, 6])