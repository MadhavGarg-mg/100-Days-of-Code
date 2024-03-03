"""I am building a blind bidding platform for day 9."""
"""Need to configure IDE and turn on emulate terminal in output console."""

from replit import clear

print("Welcome to the secret auction program.")

more_people = True
all_bids = {}

while more_people:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    all_bids[name] = bid
    add_more = input('Are there more bidders? "y" or "n"\n')
    clear()
    if add_more == 'n':
        more_people = False

print(f"The highest bidder is {max(all_bids, key=all_bids.get)} with the bid of {max(all_bids.values())}.")
