from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    is_machine_on = True
    while is_machine_on:
        choice = input(f"What would you like? {menu.get_items()}: ")
        if choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice == "off":
            is_machine_on = False
        else:
            menu_item = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(menu.find_drink(menu_item.name)) and money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)


main()