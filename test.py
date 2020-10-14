def print_tog():
    for key in table_off_games.iterkeys():
        print(key, end='')
        for items in table_off_games[key]:
            print(items, end='')
            for values in table_off_games[key][items]:
                print(values, end='')
                

table_off_games = {'Спартак': {'number_of_games': 2, 'victory': 0, 'drawn': 0, 'defeat': 2,     'game_points': 0},
                    'Зенит': {'number_of_games': 2, 'victory': 1, 'drawn': 0, 'defeat': 1, 'game_points': 3}, 
                    'Локомотив': {'number_of_games': 1, 'victory': 1, 'drawn': 0, 'defeat': 0, 'game_points': 3}}