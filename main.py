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

def simpleL(sideLength):
  casper.forward(sideLength)
  casper.left(45)
  casper.forward(sideLength)

def simpleL2(sideLength):
  jurgen.forward(sideLength)
  jurgen.left(45)
  jurgen.forward(sideLength)  

simpleL(50)
jurgen.goto(80,0)
simpleL2(50)


