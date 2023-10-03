# Ladder if else if
# Enter 3 grades (math, english, physics)
# Calculate the average.
# Consider the rank based on the average:
# Fail: average < 5, pass: 5 <= average < 7, 
# Merit: 7 <= average < 8, distinction: 8 <= average <= 10
# Print the rank with the average

math = int(input('Enter math grade: '))
english = int(input('Enter english grade: '))
physics = int(input('Enter physics grade: '))

if math < 0 or math > 10 or english < 0 or english > 10 or physics < 0 or physics > 10:
    print('Grade must be between 0 and 10')
else:
    average = (math + english + physics) / 3
    if average < 5:
        rank = 'Fail'
    elif average < 7:
        rank = 'Pass'
    elif average < 8:
        rank = 'Merit'
    else:
        rank = 'Distinction'
    print(f'Average: {average:.2f}, Rank: {rank}')