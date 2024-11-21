team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 41
score_2 = 40
team1_time = 8015.2
team2_time = 18015.2
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

print('В команде %s участников: %s' %(team1, team1_num))

print('Итого сегодня в командах участников: %s и %s' %(team1_num, team2_num))

print('Команда {0} решила задач: {1}' .format(team2, score_2))

print('{0} решили задачи за {1} с!' .format(team2, team2_time))

print(f'Команды решили {score_1} и {score_2} задач.')

print(f'Результат битвы: {challenge_result}.')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

