name = input('Enter your name: ')
language = input('Enter your programming language: ')
years = int(input('Enter years of experience: '))

if language != 'C' and language != 'Java':
    print('We are looking for C and Java programmers')
elif years < 0:
    print('Years of experience must be positive')
else:
    if language == 'C':
        project = 'System project'
    else:
        project = 'Web project'

    if years < 2:
        position = 'Junior'
    elif years < 5:
        position = 'Senior'
    else:
        position = 'Team Leader'

    print(f'Welcom {name}!')
    print(f'You will join {project} as {position}')
