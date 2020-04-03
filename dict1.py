def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif 2 * key in d:
        d[key * 2].append(value)
    else:
        d[2 * key] = [value]

update_dictionary({2: [-1, -2]}, 1, -3)