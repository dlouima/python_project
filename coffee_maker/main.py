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


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            return False
    return True


def process_coins():
    print('Please insert coins.')
    total = int(input('How many quarters?'))*0.25
    total += int(input('How many dimes?'))*0.10
    total += int(input('How many nickel? '))*0.5
    total += int(input('How many pennies? '))*0.1
    return total


def check_fund(payment, drink_cost):
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f'He is {change} in change')
        global profit
        profit = drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] - order_ingredients[item]
    return print(f" Here your {drink_name} ")


profit = 0
is_on = False

while is_on == False:
    choice = input("what would you like ? (espresso, latter or cappuccino): ")

    if choice == 'off':
        is_on = True
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        drink_cost = drink['cost']
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if check_fund(payment, drink_cost):
                make_coffee(choice, drink['ingredients'])
