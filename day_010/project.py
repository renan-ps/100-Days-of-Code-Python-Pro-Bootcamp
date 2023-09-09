from replit import clear

# Calculadora

def add(a, b):
    """Soma dois valores"""
    return a + b

def sub(a, b):
    """Subtrai dois valores"""
    return a - b

def mult(a, b):
    """Multiplica dois valores"""
    return a * b

def div(a, b):
    """Divide dois valores"""
    return a / b

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

num1 = float(input("Qual o primeiro número? "))
for symbol in operations:
    print(symbol)
operation = input("Escolha qual operação deseja fazer: ")
num2 = float(input("Qual o segundo número? "))

result = operations[operation](num1, num2)

print(f"{num1} {operation} {num2} = {result}")

cont = input("Deseja continuar calculando? ('s' ou 'n') ")
while cont == "s":
    clear()
    print(f"O resultado atual é: {result}")
    for symbol in operations:
        print(symbol)
    next_operation = input("Escolha qual a próxima operação: ")
    next_number = float(input("Qual o próximo número? "))
    next_result = operations[next_operation](result, next_number)

    print(f"{result} {next_operation} {next_number} = {next_result}")
    result = next_result
    cont = input("Deseja continuar calculando? ('s' ou 'n') ")

print(f"O resultado final é {result}")