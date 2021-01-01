# Variables with Turtle Pt.2

# Remember to import turtle
import turtle

# Let's do the same thing as before, but now we use different pen sizes
# Using turtle (pen) with different colours, red, green & blue
# Let's also change the pen size, (thickness of the pen which affects thickness of line)

# let's use variables to set the small pen size, medium pen size and large pen size
small_pen_size = 5

medium_pen_size = small_pen_size * 2

large_pen_size = medium_pen_size * 2

red_pen = turtle.Turtle()
red_pen.color("red")
# Set the red pen to the smallest size
red_pen.pensize(small_pen_size)

green_pen = turtle.Turtle()
green_pen.color("green")
# Set the green pen to the medium size
green_pen.pensize(medium_pen_size)

blue_pen = turtle.Turtle()
blue_pen.color("blue")
# Set the blue pen to the large size
blue_pen.pensize(large_pen_size)

# With different variables you can create different instances of the pen from turtle

# Move red pen forward 100 pixels
red_pen.forward(100) 

# Move green pen backward 100 pixels
green_pen.backward(100) 

# Turn blue pen left (counter-clockwise) 90 degrees 
blue_pen.left(90)

# Then move blue pen 100 pixels
blue_pen.forward(100)

# only close the window if click on screen
turtle.exitonclick()