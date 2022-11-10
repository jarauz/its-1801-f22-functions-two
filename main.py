"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

casper = turtle.Turtle()
casper.shape("turtle")

jurgen = turtle.Turtle()
jurgen.shape("triangle")

# for c in ['red', 'green', 'blue', 'yellow']:
#     t.color(c)
#     t.forward(75)
#     t.left(90)

def simpleL(turtleName, sideLength):
  turtleName.forward(sideLength)
  turtleName.left(45)
  turtleName.forward(sideLength)

# The function above now takes two arguments
# First: the name of the turtle we want to move
# Second: the side length for the drawing
# turtleName and sideLength are now variables
# that you can use inside simpleL, 
# BUT NOWHERE ELSE
simpleL(casper, 50)
jurgen.goto(70,0)
simpleL(jurgen, 60)



