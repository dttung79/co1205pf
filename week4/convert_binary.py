n = int(input('Enter number n: '))

output = ''

while n > 0:
    r = n % 2
    output = str(r) + output
    n = n // 2

print(f'{n} in binary is {output}')