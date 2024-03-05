"""I am making a higher and lower game."""
import higher_lower_data
import random
print("Welcome to the higher and lower game.")

while True:
    num1 = random.randint(0, 49)
    num2 = random.randint(0, 49)

    while num2 == num1:
        num2 = random.randint(0, 49)

    num_list = []
    num_list += [num1]
    num_list += [num2]

    option1 = higher_lower_data.data[num1]
    option2 = higher_lower_data.data[num2]

    score = 0
    while True:
        num3 = random.randint(0, 49)
        if len(num_list) < 49:  # This makes so same choices don't come often.
            while num3 in num_list:
                num3 = random.randint(0, 49)
        else:
            num_list = []
        num_list += [num3]

        print(f'Option 1: {option1["name"]}, a {option1["description"]} from {option1["country"]}')
        print('VS')
        print(f'Option 2: {option2["name"]}, a {option2["description"]} from {option2["country"]}')

        user_input = int(input('Who has more Instagram followers?: 1 or 2\n'))

        while user_input != 1 and user_input != 2:
            print('Invalid input.')
            user_input = int(input('Who has more Instagram followers?: 1 or 2\n'))

        if option1["follower_count"] > option2["follower_count"] and user_input == 1:
            print('You got it right\n')
            option1 = option2
            option2 = higher_lower_data.data[num3]
            score += 1
        elif option2["follower_count"] > option1["follower_count"] and user_input == 2:
            print('You got it right\n')
            option1 = option2
            option2 = higher_lower_data.data[num3]
            score += 1
        else:
            print('Sorry you got it wrong.')
            print(f'Option 1: {option1["name"]} has {option1["follower_count"]}M followers.')
            print(f'Option 2: {option2["name"]} has {option2["follower_count"]}M followers.')
            print(f'Your score is {score}.')
            break

    play_again = input('Play again? Y or N: \n').lower()
    while play_again not in ['y', 'n']:
        play_again = input('Play again? Y or N: \n').lower()
    if play_again != 'y':
        print('Thank you for playing higher lower game.')
        break
