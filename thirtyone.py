treasures = ["Gold", "Silver", "Gem", "Gold"]
upper_treasure = []
for treasure in treasures:
    upper_treasure.append(treasure.upper())
# Task 1: Use a list comprehesion to capitalize all treasures.
capitalized_treasures = [treasure.upper() for treasure in treasures]
print(capitalized_treasures)