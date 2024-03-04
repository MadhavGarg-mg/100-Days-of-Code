"""I am making a calculator today"""

first_number = float(input('Choose the first number:\n'))
chosen_operator = input('Choose an operation which you want to perform: +, -, *, /\n')
operators = ['+', '-', '*', '/']
if chosen_operator not in operators:
    print('Invalid operator!')
    chosen_operator = input('Choose an operation which you want to perform: +, -, *, /\n')
second_number = float(input('Choose the second number:\n'))


def calc(num1: float, num2: float, operator: str) -> float:
    """This function can do the basic calculations"""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2


while True:
    answer = calc(first_number, second_number, chosen_operator)
    print(f'{first_number} {chosen_operator} {second_number} = {answer}.')
    user_continue = input('Would you like to make more calculations with the answer?'
                          ' Y or N\n').lower()
    while user_continue != 'n':
        if user_continue == 'n':
            print('Thank you for using the calculator.')
            print('Hope to see you soon.')
            break
        elif user_continue == 'y':
            first_number = answer
            chosen_operator = input('Choose an operation which you want to perform: +, -, *, /\n')
            second_number = float(input('Choose the number:\n'))
            answer = calc(first_number, second_number, chosen_operator)
            print(f'{first_number} {chosen_operator} {second_number} = {answer}.')
            user_continue = input('Would you like to make more calculations with the answer?'
                                  ' Y or N\n').lower()
        else:
            print('Invalid input.')
            user_continue = input('Would you like to make more calculations with the answer?'
                                  ' Y or N\n').lower()
    else:
        break
