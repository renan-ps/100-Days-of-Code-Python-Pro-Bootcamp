# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# print(random_float * 5)

states_of_america = ["Delawere", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]

states_of_america[1] = "Pencilvania"

states_of_america.append("Massachusetts")

states_of_america.extend(["Maryland", "Vermont"])

print(len(states_of_america))

print(states_of_america)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[0][1])

