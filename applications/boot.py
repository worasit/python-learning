from turtle import *

brush = Turtle()
brush.speed(12)
bgcolor("Blue Violet")
brush.pensize(1)
brush.penup()

colors = ['Medium Purple', 'green', 'blue', 'orange', 'purple', 'pink', 'yellow']

brush.color('White')


def estrell():
    brush.pendown()
    brush.begin_fill()
    for i in range(5):
        brush.forward(20)
        brush.right(29)
    brush.end_fill()
    brush.penup()


for y in range(310, -300, -60):
    for x in range(-310, 300, 60):
        brush.goto(x, y)
        estrell()

for y in range(280, -300, 60):
    for x in range(-280, 300, 60):
        brush.goto(x, y)
        estrell()

done()
