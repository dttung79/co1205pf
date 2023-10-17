import turtle as t

n = int(input('Enter n: '))
angle = 360 / n
length = 100

for i in range(1, n + 1):
    #t.pencolor((255, 0, 0))
    t.forward(length)
    t.backward(length)
    t.right(angle)


t.exitonclick()