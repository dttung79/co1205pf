a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
op = input('Enter operator (+, -, *, /): ')

if op == '+':
    print(f'{a} + {b} = {a + b}')
elif op == '-':
    print(f'{a} - {b} = {a - b}')
elif op == '*':
    print(f'{a} * {b} = {a * b}')
elif op == '/':
    print(f'{a} / {b} = {a / b}')
else:
    print('Not supported operator')