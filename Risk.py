import json
import random


def save():
    with open("Data/Players.json", "w") as file:
        json.dump(players, file, indent=1)
    with open("Data/Continents.json", "w") as file:
        json.dump(continents, file, indent=1)


with open("Data/Players.json") as file:
    players = json.load(file)
with open("Data/Continents.json") as file:
    continents = json.load(file)

# Deal out and set up territories
for continent_val in continents.values():
    for territory_val in continent_val["Territories"].values():
        territory_val["Owner"] = random.choice(list(players.keys()))
        territory_val["Armies"] = 1

print(len(
    [territory_val["Owner"]
     for continent_val in continents.values()
     for territory_val in continent_val["Territories"].values()]
))
# Main game loop, continues as long as no one rules the world
while not (len(set(
        territory_val["Owner"]
        for continent_val in continents.values
        for territory_val in continent_val["Territories"].values()
))) == 1:
    pass
