"""Creating a password generator is the goal for day 5"""
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
letter_no = int(input("How many letters would you like in your password? \n"))
symbol_no = int(input(f"How many symbols would you like? \n"))
number_no = int(input(f"How many numbers would you like? \n"))

password = []
for i in range(0, letter_no):
    password += random.choice(letters)

for i in range(0, symbol_no):
    password += random.choice(symbols)

for i in range(0, number_no):
    password += random.choice(numbers)

total_length = number_no + symbol_no + letter_no
random_password = ''

for i in range(0, total_length):
    random_password += random.choice(password)
    password.remove(random_password[-1]) # This removes the used letter, number, or symbol from password

print(random_password)
