import random
import forca_art as fa
import forca_words as fw
from replit import clear

lifes = 6


#Seleciona uma palavra aleatoriamente
chosen_word = random.choice(fw.word_list)
word_length = len(chosen_word)
display = []
chosen_letters = []

#Cria o display com vários underlines
for l in chosen_word:
  display.append("_")
  


stop_loop = False

print(fa.logo)

while stop_loop == False:
  print(fa.stages[lifes])
  letter = input("Escolha uma letra: ").lower()


  while letter in chosen_letters:
    print(f"Você já escolheu a letra \"{letter}\". Por favor, escolha outra.")
    letter = input("Escolha uma letra: ").lower()

  clear()
  
  chosen_letters.append(letter)
    
    
  for position in range(word_length):
    if chosen_word[position] == letter:
      display[position] = letter
    
  if letter not in chosen_word:
    lifes -= 1
    print(f"Você escolheu a letra '{letter}' e errou. Você perdeu uma vida.")
  else:
    print(f"Você escolheu a letra '{letter}' e acertou! Continue assim!")

  display_bf = ""
  for l in display:
    display_bf += l + " "
  
  print(display_bf)
  
  #Venceu
  if "_" not in display:
    stop_loop = True
    print("Você venceu!")

  #Perdeu
  if lifes == 0:
    stop_loop = True
    print("Você perdeu!")