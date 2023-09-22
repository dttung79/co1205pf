# draw a bowtie

import turtle as t


length = 100
t.pensize(4)

# Draw 1st square with yellow fill
t.fillcolor('yellow')
t.begin_fill()
t.goto(100, 0)
t.goto(100, 100)
t.goto(0, 100)
t.goto(0, 0)
t.end_fill()

# Draw 2nd square with blue fill
t.fillcolor('blue')
t.begin_fill()
t.goto(0, -100)
t.goto(-100, -100)
t.goto(-100, 0)
t.goto(0, 0)
t.end_fill()

t.exitonclick()
