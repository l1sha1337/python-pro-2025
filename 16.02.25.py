count = int(input("Введите количество яблок "))
summ = 0
count2 = 0
while count != 0:
    weight = int(input("Введите вес яблока в граммах "))
    if weight < 150 or weight > 200:
        summ = summ + weight
        count2 = count2 + 1
    count -= 1
print("Остальые я забираю себе")
print(summ,"грамм, ", count2,"яблок", "осталось детям")