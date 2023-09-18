from random import choice
from game_data import data
from art import vs, logo
from replit import clear


def new_question():
    person_one = choice(data)
    person_two = choice(data)
    while person_one == person_two:
        person_two = choice(data)
        
    print(f"Person A: {person_one['name']}, {person_one['description']}, from {person_one['country']}")
    print(vs)
    print(f"\nPerson B: {person_two['name']}, {person_two['description']}, from {person_two['country']}")
    
    return person_one, person_two

def game():
    score = 0
    while True:
        clear()
        person_one, person_two = new_question()
        print(f"\nYour score: {score}\n")
        answer = input("Who has the most followers on Instagram? ").lower()
        
        if answer == "a" and person_one['follower_count'] > person_two['follower_count']:
            score += 1

        elif answer == "b" and person_one['follower_count'] < person_two['follower_count']:
            score += 1
        
        else:
            print(f"Game Over! Your score: {score}")
            break
            
while True:
    game()
    cont_game = input("Restart? (y or n) ").lower()
    if cont_game != "y":
        break