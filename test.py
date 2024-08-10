import turtle
from turtle import Turtle

t = Turtle()
STEPS = 10
DEGREE = 10


def move_forward():
    """moves the turtle forward"""
    t.forward(STEPS)


def move_backward():
    """moves the turtle backward"""
    t.backward(STEPS)


def turn_right():
    """turns the turtle right"""
    t.right(DEGREE)


def turn_left():
    """turns the turtle left"""
    t.left(DEGREE)


def reset_turtle():
    """reset the turtle"""
    t.reset()


turtle.listen()
turtle.onkeypress(fun=move_forward, key="Up")
turtle.onkeypress(fun=move_backward, key="Down")
turtle.onkeypress(fun=turn_right, key="Right")
turtle.onkeypress(fun=turn_left, key="Left")
turtle.onkeypress(fun=reset_turtle, key="r")
turtle.mainloop()
