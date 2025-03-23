question = int(input('Напишите вес '))
if question < 60:
    print('Легкий вес')
elif question < 64:
    print('Первый полусредний вес')
elif question < 69:
    print('Полусредний вес')
else:
    print('сколько дошиков ты съел')