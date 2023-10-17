print('square of asterisks')
n = int(input('Enter n: '))
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

print('rectangle of asterisks')
m = int(input('Enter m: '))
for i in range(n):
    for j in range(m):
        print('*', end=' ')
    print()

print('triangle of asterisks')
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()

print('reversed triangle of asterisks')
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

print('reversed triangle of asterisks, 2nd way')
for i in range(n):
    for j in range(n - i):
        print('*', end=' ')
    print()


print('right aligned triangle of asterisks')
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    print()

print('isoceles triangle of asterisks')
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end=' ')
    for j in range(2*i + 1):
        print('*', end=' ')
    print()