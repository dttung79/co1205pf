# Draw a square with color
# Ask user to enter the length & the color (choosing from red, green, blue)
# Make sure the length is between 50 and 100
# Make sure the color is one of the 3 colors above

import turtle as t

length = int(input('Enter length: '))
color = input('Enter color (red, green, blue): ')

if length < 50 or length > 100:
    print('Length must be between 50 and 100')
elif color != 'red' and color != 'green' and color != 'blue':
    print('Color must be red, green or blue')
else:
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.end_fill()

    t.exitonclick()