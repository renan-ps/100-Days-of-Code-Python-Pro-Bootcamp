print("Bem vindo à Montanha Russa")
altura = int(input("Qual a sua altura em cm?"))
conta = 0

if altura > 120:
  print("Você pode andar na montanha russa")
  idade = int(input("Qual a sua idade?"))
  if idade < 12:
    conta = 5
    print("O valor do ingresso é R$5,00")
  elif idade <= 18:
    conta = 7
    print("O valor do ingresso é R$7,00")
  else:
    if idade >= 45 and idade <= 55:
      print("O ingresso é gratuito!")
    else:
      conta = 12
      print("O valor do ingresso é R$12,00")
  
  comprar_foto = input("Você deseja comprar uma foto? (S ou N)")
  if comprar_foto == "S":
    conta += 3
    print(f"Valor total da conta: R${conta}")
  

else:
  print("Você NÃO pode andar na montanha russa")
