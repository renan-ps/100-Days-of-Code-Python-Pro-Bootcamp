#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao PyPassword Generator!")
nr_letters= int(input("Quantas letras você deseja utilizar?\n")) 
nr_symbols = int(input("Quantos simbolos você deseja utilizar?\n"))
nr_numbers = int(input("Quantos números você deseja utilizar?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""
tamanho = nr_letters + nr_symbols + nr_numbers


for n in range(1, tamanho + 1):
  type = random.randint(1, 3)
  if type == 1:
    if nr_letters > 0:
      num = random.randint(0, len(letters) - 1)
      password = password + letters[num]
      nr_letters -= 1
    else:
      if nr_symbols > 0:
        num = random.randint(0, len(symbols) - 1)
        password = password + symbols[num]
        nr_symbols -= 1
      else:
        num = random.randint(0, len(numbers) - 1)
        password = password + numbers[num]
        nr_numbers -= 1
  
  elif type == 2:
    if nr_symbols > 0:
      num = random.randint(0, len(symbols) - 1)
      password = password + symbols[num]
      nr_symbols -= 1
    else:
      if nr_numbers > 0:
        num = random.randint(0, len(numbers) - 1)
        password = password + numbers[num]
        nr_numbers -= 1
      else:
        num = random.randint(0, len(letters) - 1)
        password = password + letters[num]
        nr_letters -= 1

  else:
    if nr_numbers > 0:
      num = random.randint(0, len(numbers) - 1)
      password = password + numbers[num]
      nr_numbers -= 1
    else:
      if nr_letters > 0:
        num = random.randint(0, len(letters) - 1)
        password = password + letters[num]
        nr_letters -= 1
      else:
        num = random.randint(0, len(symbols) - 1)
        password = password + symbols[num]
        nr_symbols -= 1

print(f"\nSua senha gerada:\n{password}")