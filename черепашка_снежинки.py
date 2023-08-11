from turtle import *
from random import *


# функция, создающая снежинки
def snowflake(size, color, r, x, y):
    pensize(size)
    penup()
    goto(x, y)
    pendown()
    pencolor(color)

    for _ in range(8):

        for _ in range(3):
            forward(r / 4)
            left(45)
            forward(r * 0.1875)
            backward(r * 0.1875)
            right(90)
            forward(r * 0.1875)
            backward(r * 0.1875)
            left(45)

        forward(r / 4)
        backward(r)
        left(45)


def winter(quality):
    while True:
        answer = input('Сразу вывести результат? Введите да / нет').strip().lower()
        if answer == 'да':
            screen = Screen()
            screen.tracer(0, 0)
            # устанавливает задержку обновления экрана черепахи на 0 и отключает анимацию

            # разрешение для rgb
            # Screen().colormode(255)

            # фон
            Screen().bgcolor(choice(([255, 105, 180], [255, 165, 0])))

            # координаты снежинок
            x = list(range(-1600, 1601))
            y = list(range(-900, 900))

            # рисование снежинок
            for _ in range(quality):
                snowflake(randint(1, 5), choice(((32, 178, 170), (0, 255, 255), (64, 224, 208), (70, 130, 180),
                                                 (176, 196, 222), (123, 104, 238), (0, 0, 255), (240, 255, 255))),
                          randint(13, 50), x.pop(x.index(choice(x))), y.pop(y.index(choice(y))))
            screen.update()
            # обновляет экран автоматически
            break

        elif answer == 'нет':
            # разрешение для rgb
            # Screen().colormode(255)

            # фон
            Screen().bgcolor(choice(([255, 105, 180], [255, 165, 0])))

            # координаты снежинок
            x = list(range(-1600, 1601))
            y = list(range(-900, 900))

            # рисование снежинок
            for _ in range(quality):
                snowflake(randint(1, 5), choice(((32, 178, 170), (0, 255, 255), (64, 224, 208), (70, 130, 180),
                                                 (176, 196, 222), (123, 104, 238), (0, 0, 255), (240, 255, 255))),
                          randint(13, 50), x.pop(x.index(choice(x))), y.pop(y.index(choice(y))))
            break

        else:
            print('Я вас не понял')
            continue


winter(int(input()))


