questions = {
    'Что такое KPI?': {
        1:{'Показатель достижения успеха' : 'Верно'},
        2:{'Рейтинг зарплат сотрудников' : 'Неверно'},
        3:{'Список директоров компании' : 'Неверно'},
        4:{'Календарь отпусков' : 'Неверно'}
    }
}

print('Для окончания онбординга пройдите тестирование:')
for question in questions:
    print (question)

    for answer in questions[question]:
        q = list(questions[question][answer].keys())[0]
        print( answer,q)
        if  questions[question][answer][q] == 'Верно':
            correct_answer = answer

    reply = int(input("Номер ответа:"))
    if reply == correct_answer:
        print("Ответ верный")
    else:
        print("Ответ не верный")
        
--------------------------------------------------

questions = {
    'Что такое KPI?': {
        'Показатель достижения успеха' : 'Верно',
        'Рейтинг зарплат сотрудников' : 'Неверно',
        'Список директоров компании' : 'Неверно',
        'Календарь отпусков' : 'Неверно'
    }
}

print('Для окончания онбординга пройдите тестирование:')
for question in questions:
    print(question)
    n = 1
    for answer in questions[question]:
        print(n, answer)
        if questions[question][answer] == 'Верно':
            correct_answer = n

    reply = int(input("Номер ответа:"))
    if reply == correct_answer:
        print("Ответ верный")
    else:
        print("Ответ не верный")
        
--------------------------------------------------------


trainings = {
   'Онбординг':{
       'ответственный': 'Ершов В.С.',
       'темы': ['техника безопасности', 'работа в команде'],
       'дата': '15.05'
   },
   'Повышение квалификации':{
       'ответственный': 'Мишин Н.В.',
       'темы': ['лидерство', 'компьютерная грамотность'],
       'дата': '20.11'
   }
}
print('Тренинги ProTeam')
print('1-названия тренингов, 2-инфо о тренинге')
action = input('Номер действия (off-выйти):')
while action != 'off':
   if action == '1':
       for training in trainings:
           print('-', training)
   if action == '2':
       title = input('Название тренинга:')
       if title in trainings:
           print(trainings[title]['ответственный'])
           print(trainings[title]['темы'])
           print(trainings[title]['дата'])
       else:
           print('Такого тренинга не существует!')
   action = input('Номер действия (off-выйти):')
