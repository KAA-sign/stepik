parameters = {'number_of_games': 0, 'victory': 0, 'drawn': 0 , 'defeat': 0, 'game_points': 0}

def table_off_games(table_off_games = {}):
    teams = []
    table_off_games_interim = {}
    i = 0
    quantity = int(input('Еnter the number of games: '))
    while i < quantity:
        # team_1, score_1, team_2, score_2  = ('Спартак;9;Зенит;10').split(';')
        team_1, score_1, team_2, score_2  = input('Enter team name and score: ').split(';')
        teams = [team_1, team_2]
        for team in teams:
            if team in table_off_games.keys():
                teams.remove(team)      
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
    print(table_off_games)
table_off_games()
# print(table_off_team_set)
# print(table_off_games)
# for team, score in table_off_games.items():
#     print((team+':'), *score, end='\n')