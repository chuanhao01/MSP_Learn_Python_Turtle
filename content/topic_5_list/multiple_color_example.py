import turtle

# Let's make a list of colors
colors = ['red', 'green', 'blue', 'red']

# Print to make sure all the colors are there
print(colors)

# Drawing a square like we did in loops
pen = turtle.Turtle() # Making the pen we are using to draw
for i in range(4): # For each side to draw, i goes from 0 - 3 (position 1 -4)
    pen.color(colors[i])
    pen.forward(100) # Draw a side of 100
    pen.right(90) # Make a right turn

# Another way to do it
pen = turtle.Turtle() # Making the pen we are using to draw
for color in colors: # For each color in colors
    

turtle.exitonclick() # For VSCODE so it does not immdeiately close