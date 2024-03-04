"""Today I will be making a number guessing game"""
import random

print('Welcome to the welcome guessing game')

win_counter = 0
while True:
    level = input('What level will you like to play the game at?: easy or hard?\n')
    while level.lower() not in ['easy', 'hard']:
        print('Wrong')
        level = input('What level will you like to play the game at?: easy or hard?\n')

    attempts = 0

    number = random.randint(1, 100)

    if level.lower() == 'easy':
        attempts = 10
        print('You have 10 attempts.')
    elif level.lower() == 'hard':
        attempts = 5
        print('You have 5 attempts.')

    user_guess_list = []
    while attempts != 0:
        user_guess = int(input('What number would you like to guess between 1 and 100.\n'))
        while user_guess in user_guess_list:
            print('You already guessed this number. Try again.')
            user_guess = int(input('What number would you like to guess between 1 and 100.\n'))
        while user_guess not in range(1, 101):
            print('You did not guess between 1 and 100. Try again')
            user_guess = int(input('What number would you like to guess between 1 and 100.\n'))
        if user_guess == number:
            win_counter += 1
            print('Congratulations! You guessed the right number.')
            break
        elif -3 <= number - user_guess < 0:
            print('You need to go just a little lower')
            attempts -= 1
            print(f'You have {attempts} attempts left.')
            if attempts == 0:
                print('Sorry you lost the game is over.')
                print(f'The number was {number}')

        elif 0 < number - user_guess <= 3:
            print('You need to go just a litter higher')
            attempts -= 1
            print(f'You have {attempts} attempts left.')
            if attempts == 0:
                print('Sorry you lost the game is over.')
                print(f'The number was {number}')

        elif user_guess > number:
            print('You guessed too high.')
            attempts -= 1
            print(f'You have {attempts} attempts left.')
            if attempts == 0:
                print('Sorry you lost the game is over.')
                print(f'The number was {number}')

        elif user_guess < number:
            print('You guessed too low.')
            attempts -= 1
            print(f'You have {attempts} attempts left.')
            if attempts == 0:
                print('Sorry you lost :(')
                print(f'The number was {number}')

        user_guess_list += [user_guess]

    play_again = input('Play again? Y or N: \n').lower()
    while play_again not in ['y', 'n']:
        play_again = input('Play again? Y or N: \n').lower()
    if play_again != 'y':
        print('Thank you for playing higher or lower game.')
        print(f'You won {win_counter} game(s)')
        break
