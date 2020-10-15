
table_off_games = {'Спартак': {'number_of_games': 2, 'victory': 0, 'drawn': 0, 'defeat': 2,     'game_points': 0},
                    'Зенит': {'number_of_games': 2, 'victory': 1, 'drawn': 0, 'defeat': 1, 'game_points': 3}, 
                    'Локомотив': {'number_of_games': 1, 'victory': 1, 'drawn': 0, 'defeat': 0, 'game_points': 3}}

# def print_tog(dict_tog):
#     for key in table_off_games.keys():
#         print(key)
#         for 
    # for t in table_off_games[key][1:]:
    #     print("{:<4} {}".format(t['nomer'], t['name']))
        # for items in table_off_games[key]:
        #     print(items, end='')
        #     for values in table_off_games[key]:
        #         print(values, end='')
def print_tog(dict_tog, indent =0):
    for key, value in dict_tog.items():
        print(key, ':', end=' ')
        for key, value in value.items():
            print(value, end=' ')
        print()
print_tog(table_off_games)