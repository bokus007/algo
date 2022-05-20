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
