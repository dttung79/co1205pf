# Number operators: +, -, *, /, //, %, **
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a // b = ", a // b)
print("a % b = ", a % b)
print("a ** b = ", a ** b)

# String operators: +, *
a = 'hello'
b = 'world'
c = a + ' ' + b
print(c)

c = a + a + a
print(c)

c = a * 3
print(c)

c = 3 * a
print(c)

#c = 3 + a # error, same as a + 3
#print(c)

# Boolean operators: and, nor, not
a = True
b = False

print('a and b = ', a and b)
print('a or b = ', a or b)
print('not a = ', not a)