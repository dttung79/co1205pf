# Exercise 1:
# Ask user to enter 3 grades (math, english, physics)
# Calculate the average and print 3 grades with average

math = int(input('Enter math grade: '))
english = int(input('Enter english grade: '))
physics = int(input('Enter physics grade: '))

average = (math + english + physics) / 3
print('Math   :', f'{math:10}')
print('English:', f'{english:10}')
print('Physics:', f'{physics:10}')
print('Average:', f'{average:10.2f}')