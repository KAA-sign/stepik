with open('/home/anthony/projects/stepik/in.txt') as f:
    lst = []
    first_sum, second_sum, third_sum, count = 0, 0, 0, 0
    for line in f:
        name, first, second, third = line.split(';')
        lst.append(line.strip().split(';'))
        result = (int(first) + int(second) + int(third)) / 3
        first_sum += int(first)
        second_sum += int(second)
        third_sum += int(third)
        count += 1
        print(result)
    print((first_sum / count), (second_sum / count), (third_sum / count))


