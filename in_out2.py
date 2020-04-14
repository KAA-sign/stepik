with open('/home/anthony/projects/stepik/in.txt') as f:
    lst = []
    for line in f:
        name, first, second, third = line.split(';')
        lst.append(line.strip().split(';'))
        result = (int(first) + int(second) + int(third)) / 3
        first_sum += int(first)
        second_sum += int(second)
        third_sum += int(third)
        print(result)
    # summ = 0
    # i = 1
    # print(lst)
    # for s in lst: 
    #     for mid in s:
    #         mid = s[i]
    #      summ += int(mid)
    #  print(summ)
    #     i += 1 
    # print(summ)

# line = line.split()
#         if line and line[1][0].isdigit():
#             interface, address, *other = line
#             result[interface] = address
# result = 0
# # for line in f:
# name, first, second, third = line.split(';')
# result = (int(first) + int(second) + int(third)) / 3
# print(result)


