# On Day 19 of 100 days of code I create an etch and sketch game. This is one of a few projects for this day so feel
# free to look around at my code and have fun drawing!

# Importing modules needed
from turtle import Turtle, Screen

etch = Turtle()
etch.speed("fastest")


def forwards():
    """Moves the turtle forwards 15 paces."""
    etch.forward(15)


def backwards():
    """Moves the turtle backwards 15 paces."""
    etch.back(15)


def counter_clockwise():
    """Turns the turtle counter-clockwise 10 degrees."""
    etch.left(10)


def clockwise():
    """Turns the turtle counter 10 degrees."""
    etch.right(10)


def clear_screen():
    """Clears the screen and resets the turtle home."""
    etch.clear()
    etch.penup()
    etch.home()
    etch.pendown()


# Initialize the screen and start to listen for keystrokes
screen = Screen()
screen.listen()

# W is forwards
screen.onkeypress(key="w", fun=forwards)

# S is backwards
screen.onkeypress(key="s", fun=backwards)

# A is counter-clockwise
screen.onkeypress(key="a", fun=counter_clockwise)

# D is clockwise
screen.onkeypress(key="d", fun=clockwise)

# C, clears out the screen for a new drawing
screen.onkeypress(key="c", fun=clear_screen)

# Exits the screen on clicking the x button, or the screen.
screen.exitonclick()
