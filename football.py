
# quantity = int(input('Еnter the number of games: '))
quantity = 3
i = 0
table_off_games = {}
number_of_games, victory, drawn, defeat, game_points = 0, 0, 0, 0, 0

while i < quantity:
    # table of time template:
    #   {time: number of games, win, drawn, defeat, game_points}
    team_1, score_1, team_2, score_2  = input('Enter team name and score: ').split(';')
    # team_1, score_1, team_2, score_2  = ('Спартак;9;Зенит;10').split(';')
    if int(score_1) > int(score_2):
        table_off_games[team_1] = [number_of_games + 1, victory + 1, drawn, defeat, game_points + 3]
        table_off_games[team_2] = [number_of_games + 1, victory, drawn, defeat +1, game_points]
    elif int(score_1) < int(score_2):    
        table_off_games[team_2] = [number_of_games + 1, victory + 1, drawn, defeat, game_points + 3]
        table_off_games[team_1] = [number_of_games + 1, victory, drawn, defeat +1, game_points]
    else:
        table_off_games[team_2] = [number_of_games + 1, victory, drawn + 1, defeat, game_points + 1]
        table_off_games[team_2] = [number_of_games + 1, victory, drawn + 1, defeat, game_points + 1]
    i += 1

for team, score in table_off_games.items():
    print((team+':'), *score, end='\n')