"""Creating a function to keep if a number is prime."""

def prime_checker(number: int) -> None:
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
            break
        if i == number - 1:
            print("It's a prime number.")

n = int(input("Please type the number to want to get checked.\n"))
prime_checker(number=n)
