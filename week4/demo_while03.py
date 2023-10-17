import random as rd

answer = 'y'
n_wrong = 0
n_correct = 0

while answer == 'y':
    n = rd.randint(1, 5)
    guess_number = int(input('Enter your guess (1-5): '))
    if guess_number == n:
        print('Correct!')
        n_correct += 1
    else:
        print(f'Incorrect, the number is {n}')
        n_wrong += 1
    
    answer = input('Do you want to play again (y/n): ')

print(f'Number of incorrect guess: {n_wrong}')
print(f'Number of correct guess: {n_correct}')

print('Goodbye!')