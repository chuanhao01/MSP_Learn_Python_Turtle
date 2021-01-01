# Setup Turtle
import turtle
pen =  turtle.Turtle()

# Now that you have seen what a function is let's explore what are function parameters
# This is a way to repeat your code while changes things slightly
# For example drawing different sizes of squares

# Lets look at how we declare function
# Notice the different in this example is that in the previously empty (), we now have a variable in there called square_length
# Notice how we can also use the variable square_length in the function now
def draw_square(square_length):
    # Code that the function will run
    for _ in range(4): # For each side of the square
        pen.forward(square_length) # This pen is from outside the function
        pen.right(90)

# Lets look at how we call the funciton now
# In this example we now have to give a number when we call the function
# This is called passing in the parameter of the function, in this case it is the length of the square
draw_square(100)

# Notice now we can control the size of the square just by changing what goes into the function parameters?
draw_square(50)

# Let's expand this conept to include the pen as well (We can pass in any type of variables)
# We can also pass in multiple parameters into a function
# Also notice how here when we passing in pen, it becomes p 
def draw_square_with_pen(p, square_length):
    # Code that the function will run
    for _ in range(4): # For each side of the square
        p.forward(square_length) # This pen is from outside the function
        p.right(90)

# Calling the function with different square sizes
draw_square_with_pen(pen, 100)
draw_square_with_pen(pen, 50)

# Let's see what happens when we use a different pen
pen_2 = turtle.Turtle()
pen_2.color('red') # Changing the pen color so you can see the difference

# Notice how with this example, a different square is drawn with a different pen because we passed the different pen into the function
draw_square_with_pen(pen_2, -100)

turtle.exitonclick() # For VSCODE so it does not immdeiately close