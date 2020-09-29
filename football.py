'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15


Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6

'''


# quantity = int(input('Еnter the number of games: '))
quantity = 3
i = 0
table_off_team_set = set()
table_off_games = {}
number_of_games, victory, drawn, defeat, game_points = 0, 0, 0, 0, 0
parameters = [number_of_games, victory, drawn, defeat, game_points]

while i < quantity:
    # team_1, score_1, team_2, score_2  = input('Enter team name and score: ').split(';')
    team_1, score_1, team_2, score_2  = ('Спартак;9;Зенит;10').split(';')
    table_off_games.setdefault(team_1, parameters) 
    table_off_games.setdefault(team_2, parameters)
    if int(score_1) > int(score_2):
        table_off_games[team_1] = parameters
        parameters[0] = 1
        table_off_games[team_2] = 1
    #     elif int(score_1) < int(score_2):    
    #         table_off_games[team_2] = [number_of_games + 1, victory + 1, drawn, defeat, game_points + 3]
    #         table_off_games[team_1] = [number_of_games + 1, victory, drawn, defeat +1, game_points]
    #     else:
    #         table_off_games[team_2] = [number_of_games + 1, victory, drawn + 1, defeat, game_points + 1]
    #         table_off_games[team_2] = [number_of_games + 1, victory, drawn + 1, defeat, game_points + 1]
    i += 1    
print(table_off_team_set)
print(table_off_games)
# for team, score in table_off_games.items():
#     print((team+':'), *score, end='\n')