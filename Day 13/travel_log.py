"""Making a travel log with country, number of visits, and cities visited"""

country = input("Add country name.\n")
visits = int(input("Number of visits.\n"))
list_of_cities = eval(input("What are the cities you have visited?\n"))

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country_name: str, num_visits: int, cities: list[str]):
  travel_log.append({"country": country_name, "visits": num_visits, "cities": cities})


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

"""Test data
country -> Brazil
visits -> 2
cities -> ["Sao Paulo", "Rio de Janeiro"]
"""
