
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Three-Floor Mansion Drawing")
screen.bgcolor("skyblue")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(3)

# Function to draw a rectangle (for walls, doors, etc.)
def draw_rectangle(width, height, color):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# Function to draw a triangle (for roofs)
def draw_triangle(base, height, color):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.forward(base)
    pen.left(135)
    pen.forward(250)
    pen.left(90)
    pen.forward(200)
    pen.left(135)
    pen.end_fill()

# Function to draw windows (simple rectangles)
def draw_window(width, height, color):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# Draw the first floor (bottom)
pen.penup()
pen.goto(-150, -150)  # Starting position for the first floor
pen.pendown()
draw_rectangle(300, 100, "lightgray")

# Draw the second floor (middle)
pen.penup()
pen.goto(-150, -50)  # Starting position for the second floor
pen.pendown()
draw_rectangle(300, 100, "lightgray")

# Draw the third floor (top)
pen.penup()
pen.goto(-150, 50)  # Starting position for the third floor
pen.pendown()
draw_rectangle(300, 100, "lightgray")

# Draw the roof (triangle)
pen.penup()
pen.goto(-170, 150)
pen.pendown()
draw_triangle(340, 100, "brown")

# Draw the door on the first floor
pen.penup()
pen.goto(-30, -150)
pen.pendown()
draw_rectangle(60, 80, "darkred")

# Draw windows on the first floor
pen.penup()
pen.goto(-120, -120)
pen.pendown()
draw_window(40, 50, "lightblue")

pen.penup()
pen.goto(60, -120)
pen.pendown()
draw_window(40, 50, "lightblue")

# Draw windows on the second floor
pen.penup()
pen.goto(-120, -20)
pen.pendown()
draw_window(40, 50, "lightblue")

pen.penup()
pen.goto(60, -20)
pen.pendown()
draw_window(40, 50, "lightblue")

# Draw windows on the third floor
pen.penup()
pen.goto(-120, 80)
pen.pendown()
draw_window(40, 50, "lightblue")

pen.penup()
pen.goto(60, 80)
pen.pendown()
draw_window(40, 50, "lightblue")

# Hide the turtle
pen.hideturtle()

# Keep the window open until clicked
screen.exitonclick()