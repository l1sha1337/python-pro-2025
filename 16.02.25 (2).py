estimation = 0
counter = 0
vvod = input("Введите оценки доминика ")
while vvod != "стоп":
    num = int(vvod)
    estimation = (estimation + num)
    counter = counter + 1
    vvod = input("Введите оценки доминика ")
print("Балл Доминика", estimation / counter )