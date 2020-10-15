def height_table(tsv_file_in):
    with open(tsv_file_in) as f:
        ht = {}
        classs, _, height = '', None, []
        for line in f:
            classs, _, height = (i.rstrip() for i in line.split('\t'))
            if classs not in ht:
                ht[classs] = [height]
            else:    
                ht[classs].append(height)
    print(ht)
    return ht

def medium_height_table(ht):
    mht = {}
    cllass = 1
    for key, value in ht.items():
        for cllass in range(12):
            if cllass == key:
                for v in value:
                    count, summ = 0, 0
                    summ += int(v)
                    count += 1
                    mht[key] = summ / count
            else:
                mht[cllass] = '-'
            cllass += 1
        
    cllass += 1 
    print(mht)
    return mht
                    
                    
    #     ht = {classs: {key:value for key, value in parameters.items()} for team in teams}
    #     lst.append(line.strip().split(';'))
    #     result = (int(first) + int(second) + int(third)) / 3
    #     first_sum += int(first)
    #     second_sum += int(second)
    #     third_sum += int(third)
    #     count += 1
    #     print(result)
    # print((first_sum / count), (second_sum / count), (third_sum / count))
    
ht = height_table('/home/anthony/projects/stepik/dataset_3380_5.txt')
mht = medium_height_table(ht)   