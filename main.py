# On Day 19 of 100 days of code I create an etch and sketch game. This is one of a few projects for this day so feel
# free to look around at my code and have fun drawing!

# Importing modules needed
from turtle import Turtle, Screen

etch = Turtle()

# TODO: Create functions for each key stroke


def forwards():
    pass


def backwards():
    pass


def counter_clockwise():
    pass


def clockwise():
    pass


def clear_screen():
    pass


# TODO: Create key strokes for directions
screen = Screen()
screen.listen()

# W is forwards
screen.onkey(key="w", fun=forwards)

# S is backwards
screen.onkey(key="s", fun=backwards)

# A is counter-clockwise
screen.onkey(key="a", fun=counter_clockwise)

# D is clockwise
screen.onkey(key="d", fun=clockwise)

# C, clears out the screen for a new drawing
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()