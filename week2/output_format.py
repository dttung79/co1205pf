# without format, python reserved just enough spaces to print
s = 'hello'
a = 4
b = 4.32

# reserved 20 spaces to print
print(f'|{s:20}|') # by default, string is aligned on the left
print(f'|{a:20}|') # by default, numbers are aligned on the right
print(f'|{b:20}|')

# manually align output
print(f'|{s:>20}|')  # align s on the right
print(f'|{a:<20}|')  # align a on the left
print(f'|{b:^20}|')  # align b in the middle