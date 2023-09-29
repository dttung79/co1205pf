import turtle as t

# Set up the screen and turtle
t.speed(5)  # Moderate drawing speed
t.pensize(2)
# Draw the stick
t.penup()
t.goto(0, -200)
t.pendown()
t.left(90)
t.forward(100)

# Draw the circle
t.penup()
t.goto(0, -100)  # The circle's radius is 100
t.pendown()
t.right(90)
t.circle(100)

# Draw the star
t.penup()
t.goto(-70, 30)  # Move to the starting point of the star
t.pendown()
t.fillcolor("yellow")  # Color for the star
t.begin_fill()

t.forward(150)  # Length of the star's arm
t.right(144)  # Angle to make the star shape
t.forward(150)  # Length of the star's arm
t.right(144)  # Angle to make the star shape
t.forward(150)  # Length of the star's arm
t.right(144)  # Angle to make the star shape
t.forward(150)  # Length of the star's arm
t.right(144)  # Angle to make the star shape
t.forward(150)  # Length of the star's arm
t.right(144)  # Angle to make the star shape

t.end_fill()


t.exitonclick()
