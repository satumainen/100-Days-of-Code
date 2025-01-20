MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
is_machine_on = True


def is_resource_sufficient(order_ingredients):
    """Returns true when order can be made"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, not enough {item}.")
            return False #TODO does not return false
    return True

def process_coins():
    """Returns the total sum of inserted coins"""
    print("Please insert coins.")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns True if payment was successful"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry, not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} now.") #TODO fix bug

while is_machine_on:
    coffee_choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
    if coffee_choice == "off":
        is_machine_on = False
    elif coffee_choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[coffee_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(coffee_choice, drink["ingredients"])
