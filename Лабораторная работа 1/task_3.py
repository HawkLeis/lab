list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
count_players = len(list_players)
mid = count_players // 2
first_team = list_players[:mid]
second_team = list_players[mid:]

print(first_team)
print(second_team)
