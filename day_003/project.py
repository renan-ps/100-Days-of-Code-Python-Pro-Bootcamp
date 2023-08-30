print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo à Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

step1 = input("Você chegou na ilha e precisa escolher a direção. Esquerda ou direita? ").lower()

if step1 != "esquerda":
    print("Você caiu em um buraco. GAME OVER!")
    exit()

step2 = input("Caminhando, você chegou em um rio sem ponte para atravessar. Você deseja nadar ou esperar? ").lower()
if step2 != "esperar":
    print("Você resolveu nadar em direção ao castelo, mas foi ataco por jacarés e morreu. GAME OVER")
    exit()

step3 = input("Você resolveu esperar e um camponês passou de barco e deu carona até o outro lado. Chegando no castelo, você avista três portas. Por qual você entrará? Vermelha, amarela ou azul? ").lower()
if step3 == "vermelha":
    print("Você abriu a porta vermelha e lava caiu sobre você. GAME OVER.")
elif step3 == "amarela":
    print("Você cruzou a porta amarela e encontrou o tesouro abandonado. VOCÊ VENCEU!")
elif step3 == "azul":
    print("Você abriu a porta azul e trolls te aguardavam do outro lado, você foi atacado e morreu. GAME OVER.")
else:
    print("Você digitou uma cor inválida e morreu. GAME OVER.")