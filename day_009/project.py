from replit import clear
#HINT: You can call clear() to clear the output in the console.

lances = {}
cont = "sim"
nome_vencedor = ""
lance_vencedor = 0

while cont == "sim":
    nome = input("Qual o seu nome? ")
    lance = int(input("Qual o seu lance? R$"))

    lances[nome] = lance

    cont = input("Deseja continuar? ('sim' ou 'não') ")
    clear()

for key in lances:
    if lances[key] > lance_vencedor:
        lance_vencedor = lances[key]
        nome_vencedor = key

print(f"O(a) vencedor(a) é {nome_vencedor}, com o lance de R${lance_vencedor}")