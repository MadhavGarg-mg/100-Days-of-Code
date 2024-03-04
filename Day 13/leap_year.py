"""leap year checker."""

year = int(input("Please enter the year.\n"))


if year % 4 == 0:
  if (year % 100 == 0) and (year % 400 == 0):
    print("Leap year")
  elif year % 100 == 0 and (year % 400 != 0):
    print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
