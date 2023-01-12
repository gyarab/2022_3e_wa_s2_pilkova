from turtle import exitonclick
from turtle import forward, left, goto
from turtle import penup, pendown
from math import sqrt
import random


def draw_house(a):
    c = round(sqrt(2*a**2))
    
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    
    left(90+45)
    forward(c)
    left(90)

    forward(c/2)
    left(90)
    forward(c/2)
    left(90)

    forward(c)
    left(45)

    forward(a/5)


penup()
goto(-400, 0)
pendown()



for a in range(11):
    b = random.randint(10,200)
    draw_house(b)


exitonclick()