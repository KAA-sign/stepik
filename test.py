# dik = {'север': '10', 'запад': '20', 'юг': '30', 'восток': '40'}
# start_point = [0, 0]
# for k, v in dik.items():
#     if k == 'север':
#         start_point[1] += int(v)
#     elif k == 'запад':
#         start_point[0] -= int(v)
#     elif k == 'юг':
#         start_point[1] -= int(v)
#     elif k == 'восток':
#         start_point[0] += int(v)    
    
def turtle_coordinates(move = {}, step = 0):
    d = int(input())
    coordinates = {}
    for step in range(d):
        k, v = input().split()
        if k in coordinates:
            coordinates[k] += int(v)
        else:
            coordinates[k] = int(v)
        step += 1
    print(coordinates)

turtle_coordinates()  
        
        
    