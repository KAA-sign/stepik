with open('/home/anthony/projects/stepik/in.txt') as f:
    lst = [ ]
    for line in f:
       lst.append(line.split(';'))
print(lst)