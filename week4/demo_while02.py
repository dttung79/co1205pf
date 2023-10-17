s = 0
n = int(input('Enter an even number: '))
while n % 2 != 1:
    s += n
    n = int(input('Enter an even number: '))

print(f'Sum of entered numbers: {s}')