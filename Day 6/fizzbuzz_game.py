"""This is the Fizz Buzz game"""

for i in range(1, 100 + 1):
  if i % 5 == 0 and i % 3 == 0:
    print("FizzBuzz")
  elif i % 5 == 0:
    print("Buzz")
  elif i % 3 == 0:
    print("Fizz")
  else:
    print(i)