# For this topic we will start out with a simple implementation in the console.

# In python and turtle, you may realise we sometimes want to reapeat a certain section of code multiple times
# For example drawing multiple squares
# But what happens if we want to draw multiple square that have different color or different sizes?
# Also what happens if we want to draw them at different parts of our code?

# This is where a function comes in
# Actually you have been using functions all along, with the pen.forward(100) making the pen move
# This also ties in to the concept of what additional things function can do but let's start with the basic
# Notice how in the pen.forward(100) example, it makes the pen move forward every time (But for this to happen a lot of code is happening in python)

# So let's create a simple function that just allows us to do the same thing over and over
# We will be using the square example from a few topics ago

# Setting up turtle
import turtle
pen = turtle.Turtle()

# How we did it previously
for _ in range(4): # For each side of the square
    pen.forward(100)
    pen.right(90)

# Some function basics
# Just like how we want a square to be repeatly drawn a function need to be able to do this well
# As such a function can be decalred and ran
# When a function is declared, you are telling python what the function is (As in what code should be in the function)
# This does not run the code in the function (As such when we decalre the function to draw a square, it does not draw a square on the screen until we call it)
# When a function is 'called'/'ran'/'executed' by python is when the code in the function 'called'/'ran'/'executed'. (This can be called 'called'/'ran'/'executed' the function)

# Creating the function
# def -> is the keyword like for
# draw_square -> is the name you want for the function
# For now since we just want the function to repeat code we will use ()
def draw_square():
    # Code that the function will run
    # Hence we call functions the way to elegantly repeat your code
    for _ in range(4): # For each side of the square
        pen.forward(100)
        pen.right(90)

# Notice how if i wanted to draw a square I would just need to run
# At this point in the code, you can imagine it 2 different ways

# First:
# You imagine the code in the function is written at the point where your function is 'called'/'ran'/'executed'
# So instead of python trying to execute draw_square() the code in the function is copy pasted and ran here

# Second:
# When python trying to execute draw_square(), python goes to where the function is and see what is the code to be 'called'/'ran'/'executed'

# As such you can see in either scenario, the square is drawn when a function is called
draw_square()

turtle.Screen().exitonclick()