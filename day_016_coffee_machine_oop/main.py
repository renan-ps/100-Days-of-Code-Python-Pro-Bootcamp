from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coins = [1, 0.5, 0.25, 0.10, 0.5]
is_on = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_on:
    options = menu.get_items()
    select = ""
    
    while select not in ["espresso", "latte", "cappuccino", "report", "off"]:
        select = input(f"O que você deseja beber? ({options}) ")

    if select == "report":
        print("\nInformações da máquina:")
        coffee_maker.report()
        money_machine.report()

    elif select == "off":
        print("Desligando máquina.")
        is_on = False

    else:
        drink = menu.find_drink(select)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"Preço: {drink.cost}")
            payment = money_machine.make_payment(drink.cost)
            if payment:
                coffee_maker.make_coffee(drink)
        
