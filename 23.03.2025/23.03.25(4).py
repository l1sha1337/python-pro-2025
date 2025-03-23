question = input('Введите первый цвет ')
question_2 = input('Введите второй цвет ')
if (question == 'к' and question_2 == 'с') or (question == 'с' and question_2 == 'к'):
    print('Фиолетовый')
elif question == 'с' and question_2 == 'ж':
    print('Зеленый')
elif question == 'к' and question_2 == 'ж':
    print('Оранжевый')
else:
    print('Вы фиг знает что намешали')