"""This is basic sketch app using turtle graphics. Use 'w' to move forward, use 's' to move back, 'a' to left,
'd' to right, 'c' to clear screen, 'v' to change colour, 'Up' to pen up and lastly 'Down' to pen down"""
from turtle import *
import random
tim = Turtle()
screen = Screen()
colormode(255)
tim.pensize(5)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    tim.color(color)
def pen_up():
    tim.penup()

def pen_down():
    tim.pendown()

def move_forward():
    tim.fd(30)

def move_backward():
    tim.bk(30)

def move_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.onkey(key="v", fun=random_color)
screen.onkey(key="Up", fun=pen_up)
screen.onkey(key="Down", fun=pen_down)


screen.exitonclick()
