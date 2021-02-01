
import pickle
from datetime import datetime


with open('arr2.pkl', 'rb') as file:
    test_arr = pickle.load(file)


# example 1
def get_fixed_point(array, first, last):
    if first > last:
        return False
    else:
        mid = (first + last) // 2
        if array[mid] == mid:
            return mid
        elif mid < array[mid]:
            return get_fixed_point(array, first, mid-1)
        else:
            return get_fixed_point(array, mid+1, last)

    # index = -1
    # for value in test_arr:
    #     index += 1
    #     if value == index:
    #         return value
    # return False

# first, last  = 0, len(test_arr)
start = datetime.now()
result = get_fixed_point(test_arr, first=0, last=len(test_arr))
finish = datetime.now() - start
print(f'Result func1 => {result}  time: {finish}')
