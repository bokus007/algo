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
