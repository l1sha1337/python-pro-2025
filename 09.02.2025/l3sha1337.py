import random
num = random.randint(0,10)
question = int(input("Введите число "))
while num != question:
    question = int(input("Введите число "))
    print("Вы не угадали попробуйте еще раз")
print("Вы угадали")