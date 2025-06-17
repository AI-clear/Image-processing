import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Drawing a Circle on a Square")

# Create a turtle for drawing the square
square = turtle.Turtle()
square.color("blue")
square.begin_fill()
for _ in range(4):
    square.forward(200)
    square.left(90)
square.end_fill()
square.hideturtle()

# Create another turtle for drawing the circle
circle = turtle.Turtle()
circle.penup()
circle.goto(100, 0)  # Move to the starting position of the circle
circle.pendown()
circle.color("red")
circle.begin_fill()
circle.circle(100, 180)  # Draw the left semicircle in red
circle.end_fill()

circle.right(360)  # Position the turtle to draw the right semicircle
circle.penup()
circle.goto(100, 0)
circle.pendown()
circle.color("green")
circle.begin_fill()
circle.circle(-100, 180)  # Draw the right semicircle in blue
circle.end_fill()

# Hide the turtle and finish
circle.hideturtle()
wn.mainloop()
