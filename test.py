parameters = {'number_of_games': 0, 'victory': 0, 'drawn': 0 , 'defeat': 0, 'game_points': 0}
team_1, score_1, team_2, score_2  = ('Спартак;9;Зенит;10').split(';')
team = [team_1, team_2]
table_off_games = {team: {key:value for key, value in parameters.items()} for team in team}
print(table_off_games)