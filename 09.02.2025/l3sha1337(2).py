import turtle
turtle.home()
while True:
    question = input("Введитее команду ")
    if question == "поднять":
        turtle.penup()
    elif question == "опустить":
        turtle.pendown()
    elif question == "вперед":
        turtle.forward(100)
    elif question == "назад":
        turtle.backward(100)
    elif question == "направо":
        turtle.right(90)
    elif question == "налево":
        turtle.left(90)
    else:
        print("Команды выучи")
turtle.done()