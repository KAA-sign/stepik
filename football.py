def table_off_games(table_off_games = {}):
    parameters = {'number_of_games': 0, 'victory': 0, 'drawn': 0 , 'defeat': 0, 'game_points': 0}
    teams, keys_tog, table_off_games_interim = [], [], {}
    i = 0
    quantity = int(input('Еnter the number of games: '))
    while i < quantity:
        team_1, score_1, team_2, score_2  = input('Enter team name and score: ').split(';')
        teams = [team_1, team_2]
        keys_tog = list(table_off_games.keys())
        teams = list(set(teams) - set(keys_tog)) 
        table_off_games_interim = {team: {key:value for key, value in parameters.items()} for team in teams}
        table_off_games.update(table_off_games_interim)
        if int(score_1) > int(score_2):
            table_off_games[team_1]['number_of_games'] += 1 
            table_off_games[team_1]['victory'] += 1 
            table_off_games[team_1]['game_points'] += 3
            table_off_games[team_2]['number_of_games'] += 1
            table_off_games[team_2]['defeat'] += 1  
        elif int(score_1) < int(score_2):
            table_off_games[team_2]['number_of_games'] += 1 
            table_off_games[team_2]['victory'] += 1 
            table_off_games[team_2]['game_points'] += 3
            table_off_games[team_1]['number_of_games'] += 1
            table_off_games[team_1]['defeat'] += 1 
        else:
            table_off_games[team_1]['number_of_games'] += 1
            table_off_games[team_2]['number_of_games'] += 1 
            table_off_games[team_1]['game_points'] += 1
            table_off_games[team_2]['game_points'] += 1
            table_off_games[team_1]['drawn'] += 1
            table_off_games[team_2]['drawn'] += 1
        i += 1
    return table_off_games

def print_tog(dict_tog):
    for key, value in dict_tog.items():
        print(key, ':', end=' ')
        for key, value in value.items():
            print(value, end=' ')
        print()
    
tog = table_off_games()
print_tog(tog)