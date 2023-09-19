MENU = {
    "expresso": {
        "ingredientes": {
            "agua": 50,
            "leite": 0,
            "cafe": 18,
        },
        "preco": 1.5,
    },
    "media": {
        "ingredientes": {
            "agua": 200,
            "leite": 150,
            "cafe": 24,
        },
        "preco": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "leite": 100,
            "cafe": 24,
        },
        "preco": 3.0,
    },
}

profit = 0
resources = {
    "agua": 300,
    "leite": 200,
    "cafe": 100,
}

coins = [1, 0.50, 0.25, 0.10, 0.05]


def buy(product):
    global profit
    preco = MENU[product]["preco"]
    print(f"Valor do {product}: R${preco}")
    total = 0
    for _ in coins:
        partial = int(input(f"Quantidade de moedas de R${_}: ")) * _
        total = total + partial

    if total < preco:
        print(
            "Você depositou um valor inferior ao valor do produto. Devolvendo moedas."
        )
        buy(product)
    else:
        if check_resources(MENU[product]):
            troco = total - preco
            profit = preco
            print(
                f"Você depositou R${total}. Seu troco: R${troco}\nAqui está seu {product}."
            )
            menu()

        else:
            print(f"{missing_resource(MENU[product])} em falta.")
            menu()


def missing_resource(product):
    global resouces
    if resources["agua"] < product["ingredientes"]["agua"]:
        return "Água"
    elif resources["leite"] < product["ingredientes"]["leite"]:
        return "Leite"
    elif resources["cafe"] < product["ingredientes"]["cafe"]:
        return "Café"


def check_resources(product):
    global resources
    if (
        resources["agua"] < product["ingredientes"]["agua"]
        or resources["leite"] < product["ingredientes"]["leite"]
        or resources["cafe"] < product["ingredientes"]["cafe"]
    ):
        return False
    else:
        resources["agua"] -= product["ingredientes"]["agua"]
        resources["leite"] -= product["ingredientes"]["leite"]
        resources["cafe"] -= product["ingredientes"]["cafe"]
        return True


def menu():
    select = input("O que você gostaria hoje? (expresso/media/cappuccino): ")

    if select == "report":
        for _ in resources:
            print(f"{_}: {resources[_]}ml")
        menu()
    elif select == "shutdown":
        print("Desligando.")
        exit()
    else:
        buy(select)


menu()
