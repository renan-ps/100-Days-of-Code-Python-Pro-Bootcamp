# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

soma = 0
estudantes = 0

for n in student_heights:
    soma += n
    estudantes += 1

resultado = soma / estudantes

print(round(resultado))