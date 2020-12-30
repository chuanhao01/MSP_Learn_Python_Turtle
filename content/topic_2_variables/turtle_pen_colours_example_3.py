# Variables with Turtle

# Remember to import turtle
import turtle

# Let's start to draw things by getting the pen from turtle
# Using turtle (pen) with different colours, red, green & blue
red_pen = turtle.Turtle()
red_pen.color("red")

green_pen = turtle.Turtle()
green_pen.color("green")

blue_pen = turtle.Turtle()
blue_pen.color("blue")

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