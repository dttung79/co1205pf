import turtle as t

n = int(input('Enter n: '))
angle = (n - 2) * 180 / n
length = 100

for i in range(n):
    t.forward(length)
    t.left(180 - angle)


t.exitonclick()