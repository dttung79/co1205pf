# draw a square without a top

import turtle as t

# Draw 1st square
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# Move to a new location
t.penup()
t.forward(200)
t.pendown()

# Draw 2nd square
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

t.exitonclick()
