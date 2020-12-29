import turtle
import random

# List can be made empty
# It can also be 'stored' in a variable
pens = []

# Let say I want to create 10 pens
# We can use a loop
for _ in range(10):
    pens.append(turtle.Turtle())

# Look at what the list looks like now
# You can see in the console that it says some weird string of the object
# But we can see that we have 10 pens :D
print(pens)

# Example 2
# Lets make all the pens move in random directions and see what happens
for pen in pens: # This for loop is saying for each pen in pens
    pen.right(random.randint(0, 360)) # This is to make the pen rotate in a random direction in 360
    pen.forward(100)

turtle.exitonclick() # For VSCODE so it does not immdeiately close