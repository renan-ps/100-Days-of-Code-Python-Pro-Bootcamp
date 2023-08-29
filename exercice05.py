# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()
palavra1 = "true"
palavra2 = "love"
cont_palavra1 = 0
cont_palavra2 = 0

for letra1 in name1:
    for letra2 in palavra1:
        if letra2 == letra1:
            cont_palavra1 += 1

for letra1 in name1:
    for letra2 in palavra2:
        if letra2 == letra1:
            cont_palavra2 += 1


    
for letra1 in name2:
    for letra2 in palavra1:
        if letra2 == letra1:
            cont_palavra1 += 1

for letra1 in name2:
    for letra2 in palavra2:
        if letra2 == letra1:
            cont_palavra2 += 1

cont_str = str(cont_palavra1) + str(cont_palavra2)
cont_int = int(cont_str)

if cont_int < 10 or cont_int > 90:
    print(f"Your score is {cont_int}, you go together like coke and mentos.")
elif cont_int >= 40 and cont_int <= 50:
    print(f"Your score is {cont_int}, you are alright together.")
else:
    print(f"Your score is {cont_int}.")