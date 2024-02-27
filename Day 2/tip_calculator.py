"""Creating a tip calculator using input of bill, number of people and tip percentage while using
different data inputs (int) is the goal for day 2"""

bill = int(input("What is your total bill?\n"))

num_people = int(input("How many people to split the bill?\n"))

tip_percentage = int(input("What percentage tip would you like to give? 12, 15, 20\n"))

print(f"The bill for each person will be {(bill + (bill * (tip_percentage / 100))) /  num_people}")
