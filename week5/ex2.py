balance = int(input('Enter your balance to play: '))

while balance > 0:
    game = input('Enter game to play: ')
    price = int(input('Enter price per minute: '))
    playing = True

    while playing:
        minutes = int(input('Enter number of minutes to play: '))
        if price * minutes > balance:
            print('Not enough balance!')
            playing = False
        else:
            balance -= price * minutes
            print(f'Current balance: {balance}')
            answer = input(f'Do you still want to play {game} (y/n): ')
            playing = answer == 'y'