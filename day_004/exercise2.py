# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
max = len(names) - 1

random_number = random.randint(0, max)

print(f"{names[random_number]} is going to buy the meal today!")
