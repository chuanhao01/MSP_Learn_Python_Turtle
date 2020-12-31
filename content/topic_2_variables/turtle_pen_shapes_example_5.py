# Variables with Turtle Pt.3

# Remember to import turtle
import turtle

# Let's change the shape of the pen to different ones

red_pen = turtle.Turtle()
red_pen.color("red")
red_pen.shape("turtle")
# Set the red pen to the smallest size

green_pen = turtle.Turtle()
green_pen.color("green")
green_pen.shape("circle")
# Set the green pen to the medium size

blue_pen = turtle.Turtle()
blue_pen.color("blue")
blue_pen.shape("triangle")
# Set the blue pen to the large size

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