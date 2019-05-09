#!/usr/bin/env python3

import turtle

screen = turtle.Screen()
pig = turtle.Turtle()

'''畫佩佩豬'''

def nose(x, y):

    """畫鼻子"""

    pig.penup()
    # 將海龜移動到指定的座標
    pig.goto(x, y)
    pig.pendown()
    # 設置海龜的方向（0-東、90-北、180-西、270-南）
    pig.setheading(-30)
    pig.begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            # 向左轉3度
            pig.left(3)
            # 向前走
            pig.forward(a)
        else:
            a = a - 0.08
            pig.left(3)
            pig.forward(a)
    pig.end_fill()
    pig.penup()
    pig.setheading(90)
    pig.forward(25)
    pig.setheading(0)
    pig.forward(10)
    pig.pendown()
    pig.pencolor('#32c18f')
    pig.setheading(10)
    pig.begin_fill()
    pig.circle(5)
    pig.color("yellow", "")
    pig.end_fill()
    pig.penup()
    pig.setheading(0)
    pig.forward(20)
    pig.pendown()
    pig.pencolor('#32c18f')
    pig.setheading(10)
    pig.begin_fill()
    pig.circle(5)
    pig.color("yellow", "")
    pig.end_fill()


def head(x, y):

    """畫頭"""

    pig.color("pink", "")
    pig.penup()
    pig.goto(x, y)
    pig.setheading(0)
    pig.pendown()
    pig.begin_fill()
    pig.setheading(180)
    pig.circle(300, -30)
    pig.circle(100, -60)
    pig.circle(80, -100)
    pig.circle(150, -20)
    pig.circle(60, -95)
    pig.setheading(161)
    pig.circle(-300, 15)
    pig.penup()
    pig.goto(-100, 100)
    pig.pendown()
    pig.setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            pig.lt(3)  # 向左轉 3 度
            pig.fd(a)  # 向前走 a 的步長
        else:
            a = a - 0.08
            pig.lt(3)
            pig.fd(a)
    pig.end_fill()


def ears(x, y):

    """畫耳朵"""

    pig.color("pink", "")
    pig.penup()
    pig.goto(x, y)
    pig.pendown()
    pig.begin_fill()
    pig.setheading(100)
    pig.circle(-50, 50)
    pig.circle(-10, 120)
    pig.circle(-50, 54)
    pig.end_fill()
    pig.penup()
    pig.setheading(90)
    pig.forward(-12)
    pig.setheading(0)
    pig.forward(30)
    pig.pendown()
    pig.begin_fill()
    pig.setheading(100)
    pig.circle(-50, 50)
    pig.circle(-10, 120)
    pig.circle(-50, 56)
    pig.end_fill()


def eyes(x, y):

    """畫眼睛"""

    pig.color("white", "")
    pig.penup()
    pig.setheading(90)
    pig.forward(-20)
    pig.setheading(0)
    pig.forward(-95)
    pig.pendown()
    pig.begin_fill()
    pig.circle(15)
    pig.end_fill()
    pig.color("black")
    pig.penup()
    pig.setheading(90)
    pig.forward(12)
    pig.setheading(0)
    pig.forward(-3)
    pig.pendown()
    pig.begin_fill()
    pig.circle(3)
    pig.end_fill()
    pig.color("white", "")
    pig.penup()
    pig.seth(90)
    pig.forward(-25)
    pig.seth(0)
    pig.forward(40)
    pig.pendown()
    pig.begin_fill()
    pig.circle(15)
    pig.end_fill()
    pig.color("black")
    pig.penup()
    pig.setheading(90)
    pig.forward(12)
    pig.setheading(0)
    pig.forward(-3)
    pig.pendown()
    pig.begin_fill()
    pig.circle(3)
    pig.end_fill()


def cheek(x, y):

    """畫臉頰"""

    pig.color("pink")
    pig.penup()
    pig.goto(x, y)
    pig.pendown()
    pig.setheading(60)
    pig.begin_fill()
    pig.circle(30)
    pig.end_fill()


def mouth(x, y):

    """畫嘴巴"""

    pig.color("red", "")
    pig.penup()
    pig.goto(x, y)
    pig.pendown()
    pig.setheading(-80)
    pig.circle(30, 40)
    pig.circle(40, 80)


def setting():

    """設置参數"""

    pig.pensize(4)
    # 隱藏海龜
    pig.hideturtle()
#   pig.colormode(255)
    pig.color("pink", "")
#   pig.setup(840, 500)
    pig.speed(10)


def main():

    """主函數"""

    setting()
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    pig.end_fill()
    screen.exitonclick()


if __name__ == '__main__':
    main()