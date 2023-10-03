# Enter 3 sides of a triangle
# Make sure they are valid sides of a triangle 
# (greater than 0 and sum of 2 sides is greater than the other side)
# then calculate the area of the triangle and print it.

# Method 1: check valid condition first
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
# if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and c + a > b:
#     p = (a + b + c) / 2
#     s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print(f'Area of the triangle ({a}, {b}, {c}) = {s:.2f}')
# else:
#     print('Invalid sides of a triangle')

# Method 2: check invalid condition first
if a <= 0 or b <= 0 or c <= 0:
    print('Side must be greater than 0')
elif a + b <= c or b + c <= a or c + a <= b:
    print('Sum of 2 sides must be greater than the other side')
else:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f'Area of the triangle ({a}, {b}, {c}) = {s:.2f}')