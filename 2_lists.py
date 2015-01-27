# Working with lists

names_of_planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Saturn', 'Jupiter', 'Uranus', 'Neptune']



# Write code that will answer the following questions:
# ----------------------------------------------------

#### How many planets are there?

##Method 1
##print("There are", len(names_of_planets), "planets")
##print()
##
##Method 2
##planet_count = 0
##for name in names_of_planets:
##   planet_count += 1
##print("There are", planet_count, "planets")
##
##Method 3
##
##planet_count = len(names_of_planets)
##print("There are %s" % planet_count, "planets")
##

#### Display the names of the planets in alphabetical order

##names_of_planets = sorted(names_of_planets)
##print(names_of_planets)


#### Pick a planet at random
##import random
##randomPlanet = random.sample(names_of_planets, 1)
##print(randomPlanet)
##
#### Pick two planets at random
##import random
##randomPlanet = random.sample(names_of_planets, 1)
##print(randomPlanet)

#### Randomize the list
##import random
##random.shuffle(names_of_planets)
##print(names_of_planets)

#### Remove a planet from the list
##names_of_planets.remove("Earth")
##print(names_of_planets)

## Add Pluto to the list
names_of_planets.append("Pluto")
print(names_of_planets)




