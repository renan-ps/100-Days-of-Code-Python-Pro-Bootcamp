############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
cards_player = []
cards_dealer = []
cards_dealer_hidden = []
sum_player = 0
sum_dealer = 0
players = {
    "player": cards_player,
    "dealer": cards_dealer
}

def sorted_one_card():
    card_sorted = random.randint(0, 12)
    while cards[card_sorted] == "X":
        card_sorted = random.randint(0,12)
    card = cards[card_sorted]
    cards[card_sorted] = "X"
    return card

def pull_card(who):
    global sum_player, sum_dealer, players
    players[who].append(sorted_one_card())
    
    if players[who][-1] == "A":
        if who == "player":
            sum_player += 11
        else:
            sum_dealer += 11
    elif players[who][-1] in ["J", "Q", "K"]:
        if who == "player":
            sum_player += 10
        else:
            sum_dealer += 10
    else:
        if who == "player":
            sum_player += int(players[who][-1]) 
        else:
            sum_dealer += int(players[who][-1]) 

    a = False
    if sum_player > 21:
        for n in range(len(cards_player) - 1):
            if cards_player[n] == "A":
                a = True
        if a == True:
            sum_player -= 10
    
    a = False
    if sum_dealer > 21:
        for n in range(len(cards_dealer) - 1):
            if cards_dealer[n] == "A":
                a = True
        if a == True:
            sum_dealer -= 10

def initial_cards():
    
    for _ in range(1, 3):
        pull_card("player")
        pull_card("dealer")

    cards_dealer_hidden.append(cards_dealer[0])
    cards_dealer_hidden.append("X")

    results("hidden")
    verify_blackjack()
    

def ask_player():
    return input('''
Deseja continar ou parar? Escolha:
"C" para continuar 
"P" para parar
''').lower()

def results(hidden):
    if hidden == "hidden":
        print(f'''Suas cartas: {cards_player}
Seu total: {sum_player}

Cartas do dealer: {cards_dealer_hidden}
''')
    else:
        print(f'''Suas cartas: {cards_player}
Seu total: {sum_player}

Cartas do dealer: {cards_dealer}
Total do dealer: {sum_dealer}
''')

def verify_blackjack():
    global sum_player

    if sum_player == 21:
        if sum_dealer != 21:
            print("Você tem um BlackJack!\nVocê venceu!")
            exit()
        else:
            results("nohidden")
            print("Empatou!")
            exit()


initial_cards()

choice = ask_player()

while choice == "c":
    clear()
    print("Você continuou.")
    pull_card("player")
    results("hidden")

    verify_blackjack()

    if sum_player > 21:
        choice = "gameover"
        print("Você perdeu!")
    else:
        choice = ask_player()
    
if choice == "p":
    while sum_dealer < 17:
        pull_card("dealer")
        
    clear()
    print("Você parou.")
    
    if sum_dealer >= 17:
        results("nohidden")
        if sum_dealer > sum_player and sum_dealer < 22:
            print("Você perdeu!")
        elif sum_dealer < sum_player or sum_dealer > 21:
            print("Você venceu!")
        else:
            print("Empatou!")

    





##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

