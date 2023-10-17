# print the numbers from 0 to 9
for i in range(10):
    print(i, end=' ')

print('\n------------------')

# calculate the sum of the numbers from 1 to 10
s = 0
for i in range(1, 11):
    s += i # s = s + i

print(f'Sum of numbers from 1 to 10: {s}')

output = ''
for i in range(10):
    output += '*'

print(output)

# Print the multiplication table of n
n = int(input('Enter n: '))
for i in range(1, 11):
    p = i * n
    print(f'{i:2} x{n:2} = {p:2}')