import random as rd

answer = 'y'
while answer == 'y':
    n_corrects = 0
    n_incorrects = 0
    for i in range(5):
        n_random = rd.randint(1, 5)
        n_guess = int(input('Enter your guess (1-5): '))
        if n_random == n_guess:
            print('Correct!')
            n_corrects += 1
        else:
            print('Incorrect!')
            n_incorrects += 1
    
    print(f'Number of correct guess: {n_corrects}')
    print(f'Number of incorrect guess: {n_incorrects}')
    answer = input('Do you want to play again (y/n): ')