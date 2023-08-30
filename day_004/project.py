import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

escolha_jogador = int(input('''Escolha:
1 - Pedra
2 - Papel
3 - Tesoura
'''))

escolha_maquina = random.randint(1, 3)

if escolha_jogador == 1:
  print(rock)
elif escolha_jogador == 2:
  print(paper)
else:
  print(scissors)

print("Escolha do computador:")
if escolha_maquina == 1:
  print(rock)
elif escolha_maquina == 2:
  print(paper)
else:
  print(scissors)

if (escolha_jogador == 1 and escolha_maquina == 1) or (escolha_jogador == 2 and escolha_maquina == 2) or (escolha_jogador == 3 and escolha_maquina == 3):
  print("Empatou!")
elif (escolha_jogador == 1 and escolha_maquina == 2) or (escolha_jogador == 2 and escolha_maquina == 3) or (escolha_jogador == 3 and escolha_maquina == 1):
  print("Perdeu!")
else:
  print("Ganhou!")